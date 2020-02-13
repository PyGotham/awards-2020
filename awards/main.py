from typing import Any, Dict, Optional

from flask import Flask, render_template


def create_app(test_config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask("awards")
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config:
        app.config.from_mapping(test_config)

    @app.route("/")
    def home() -> str:
        return render_template("home.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
