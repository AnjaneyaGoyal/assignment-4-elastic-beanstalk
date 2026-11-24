import os
from flask import Flask, render_template_string

application = app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AWS Elastic Beanstalk Deployment - Assignment 4 (v2.0)</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 40px; border-radius: 12px; border: 1px solid #334155; text-align: center; max-width: 600px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        .badge { background: #6366f1; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 0.85rem; display: inline-block; margin-bottom: 15px; }
        .success-box { background: rgba(34, 197, 94, 0.2); border: 1px solid #22c55e; color: #4ade80; padding: 12px; border-radius: 6px; margin: 15px 0; font-size: 0.95rem; }
        h1 { color: #38bdf8; margin: 10px 0; }
        p { color: #94a3b8; line-height: 1.6; }
        .env-box { background: #0f172a; border-left: 4px solid #10b981; padding: 15px; margin: 20px 0; text-align: left; }
        .env-var { font-family: monospace; color: #34d399; font-weight: bold; font-size: 1.2rem; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">AWS Elastic Beanstalk: Auto-Updated</span>
        <div class="success-box">✓ Continuous Deployment Verified: Pipeline auto-deployed release v2.0!</div>
        <h1>PaaS Application Deployment</h1>
        <p>Continuous deployment managed via AWS CodePipeline directly to Elastic Beanstalk.</p>
        <div class="env-box">
            <p style="margin: 0 0 5px 0; color: #64748b;">Injected Environment Variable (APP_ENV):</p>
            <div class="env-var">APP_ENV = {{ app_env }}</div>
            <p style="margin: 10px 0 0 0; color: #64748b;">Author: <strong>Anjaneya Goyal</strong> | Version: <strong>{{ version }}</strong></p>
        </div>
    </div>
</body>
</html>
"""

@application.route("/")
def index():
    env_name = os.environ.get("APP_ENV", "Production")
    version = os.environ.get("DEPLOY_VERSION", "v2.0.0-Zero-Downtime")
    return render_template_string(HTML, app_env=env_name, version=version)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
