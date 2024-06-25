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