from typing import Any, Dict, Optional

from flask import Flask


def create_app(test_config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask("rewards")
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config:
        app.config.from_mapping(test_config)

    @app.route("/hello")
    def hello() -> str:
        return "hello, world"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
