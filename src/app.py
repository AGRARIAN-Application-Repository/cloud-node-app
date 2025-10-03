#!/usr/bin/env python3
"""
cloud-node-app - Agrarian Cloud Node Application
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "name": "cloud-node-app",
        "version": "1.0.0",
        "status": "running",
        "description": "Agrarian Cloud Node Application"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
