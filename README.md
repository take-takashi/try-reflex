# try-reflex

reflexを動かしてみる試み

## Install command

```sh
@take-takashi ➜ /workspaces/try-reflex (main) $ poetry new sample-reflex --src
Created package sample_reflex in sample-reflex
```

## 環境設定の方針

- 各プロジェクトに`.vscode`フォルダを作成し、設定を格納する。
- `settings.json`の大本の設定は`untitled.code-workspace`に記載する。
- pythonのFormatter, LinterはRuffを使用し、設定は`pyproject.toml`に記載する。  
  （[tool.ruff], [tool.ruff.pydocstyle]）
- `root`プロジェクトに`pytest.ini`を作成し、不要なキャッシュが作成されないようにする。  
  （もしかしたら`pyproject.toml`の方のみでいいかも）
- `pytest`のさらなるキャッシュを生成しないよう、設定を`pyproject.toml`にも記載する。  
  （[tool.pytest.ini_options]）
- 各プロジェクトの`poetry install`は`devcontainer.json`の`postCreateCommand`にワンライナーで記載した（工夫した）。
