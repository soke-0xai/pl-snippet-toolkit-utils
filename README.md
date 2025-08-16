# pl-snippet-toolkit-utils-001

高品質なPython/TypeScriptユーティリティ集。データ処理、API通信、可視化、型検証などを網羅。

## 機能一覧
- CSV処理（pandas/numpy）
- チャート生成（matplotlib/seaborn）
- REST APIクライアント（requests）
- JSON型検証（Zod）
- GraphQLクライアント（axios）
## 4User
https://pypi.org/project/pl-snippet-toolkit-utils-001/
```bash
$ pip install pl-snippet-toolkit-utils-001
```

## 4Developper
### セットアップ
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install pytest pytest-cov build twine
npm install
tsc --init # 初回のみTypeScriptプロジェクト設定
```

### テスト
```bash
pytest

# TypeScriptのテストは、src/__tests__ や src/配下に test ファイルを追加してください。
npm run test # テストファイルが無い場合はエラーになります
```

### 公開

https://pypi.org/project/pl-snippet-toolkit-utils-001/



### PyPI公開（Python）
- https://pypi.org/ でAPIトークンを取得し、公開時に入力してください。
- `pyproject.toml` の `license` はSPDX形式（例: "MIT"）推奨。警告が出る場合は修正してください。

```bash
chmod +x scripts/publish.sh
./scripts/publish.sh
```

### ライセンス
MIT
