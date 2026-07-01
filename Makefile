.PHONY: notebook kill lint lint-fix typecheck test

notebook:
	PYTHONPATH=src poetry run jupyter notebook --ServerApp.token='' --ServerApp.password='' --ServerApp.ip=127.0.0.1

kill:
	@pids=$$(lsof -tiTCP:8888 -sTCP:LISTEN 2>/dev/null || true); \
	if [ -z "$$pids" ]; then \
		echo "No process is listening on port 8888."; \
		exit 0; \
	fi; \
	echo "Sending SIGTERM to process(es) on port 8888: $$pids"; \
	kill $$pids || true; \
	remaining=$$(lsof -tiTCP:8888 -sTCP:LISTEN 2>/dev/null || true); \
	if [ -n "$$remaining" ]; then \
		echo "Still listening on 8888, sending SIGKILL: $$remaining"; \
		kill -9 $$remaining || true; \
	fi; \
	final=$$(lsof -tiTCP:8888 -sTCP:LISTEN 2>/dev/null || true); \
	if [ -n "$$final" ]; then \
		echo "Port 8888 is still in use by: $$final"; \
		exit 1; \
	else \
		echo "Port 8888 is free."; \
	fi

lint:
	poetry run ruff check src tests

lint-fix:
	poetry run ruff check --fix src tests
	poetry run ruff format src tests

typecheck:
	poetry run pyright

test:
	poetry run pytest
