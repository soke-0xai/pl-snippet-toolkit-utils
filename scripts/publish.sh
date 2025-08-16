#!/bin/bash
set -e

# 公開用スクリプト
# Python/TypeScriptパッケージのビルド・公開

# Pythonパッケージ公開
python -m build
python -m twine upload dist/*

# TypeScriptパッケージ公開
npm run build
npm publish

echo "Publish completed!"
