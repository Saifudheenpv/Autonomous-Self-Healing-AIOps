from flask import Flask, jsonify, Response
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
import time
import os

app = Flask(__name__)

# --------------------------------------------------
# Application Version
# --------------------------------------------------

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# --------------------------------------------------
# Prometheus Metrics
# --------------------------------------------------

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

ERROR_COUNT = Counter(
    "app_errors_total",
    "Total simulated application errors"
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency"
)

# --------------------------------------------------
# Internal State
# --------------------------------------------------

simulate_errors = False


# --------------------------------------------------
# Helper
# --------------------------------------------------

def record_request(method, endpoint, status):
    REQUEST_COUNT.labels(
        method=method,
        endpoint=endpoint,
        status=status
    ).inc()


# --------------------------------------------------
# Routes
# --------------------------------------------------

@app.route("/")
@REQUEST_LATENCY.time()
def home():
    if simulate_errors:
        ERROR_COUNT.inc()
        record_request("GET", "/", "500")
        return jsonify(
            status="error",
            message="Simulated application failure"
        ), 500

    record_request("GET", "/", "200")

    return jsonify(
        status="success",
        application="Autonomous Self-Healing AIOps Demo",
        version=APP_VERSION
    )


@app.route("/health")
def health():
    record_request("GET", "/health", "200")
    return jsonify(status="UP")


@app.route("/ready")
def ready():
    record_request("GET", "/ready", "200")
    return jsonify(status="READY")


@app.route("/version")
def version():
    record_request("GET", "/version", "200")
    return jsonify(version=APP_VERSION)


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


@app.route("/error")
def enable_errors():
    global simulate_errors
    simulate_errors = True

    return jsonify(
        message="Error simulation enabled"
    )


@app.route("/reset-errors")
def disable_errors():
    global simulate_errors
    simulate_errors = False

    return jsonify(
        message="Error simulation disabled"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )