import json

from voicevox_engine.dev.core import mock as core
from voicevox_engine.dev.synthesis_engine.mock import MockSynthesisEngine
from voicevox_engine.setting import USER_SETTING_PATH, SettingLoader
from huggingsound import SpeechRecognitionModel

if __name__ == "__main__":
    import run
    
    default_model = "jonatasgrosman/wav2vec2-large-xlsr-53-japanese"
    model = SpeechRecognitionModel(default_model)
    app = run.generate_app(
        synthesis_engines={"mock": MockSynthesisEngine(speakers=core.metas())},
        latest_core_version="mock",
        setting_loader=SettingLoader(USER_SETTING_PATH),
        stt_model=model
    )
    with open("docs/api/index.html", "w") as f:
        f.write(
            """<!DOCTYPE html>
<html lang="ja">
<head>
    <title>voicevox_engine API Document</title>
    <meta charset="utf-8">
    <link rel="shortcut icon" href="https://voicevox.hiroshiba.jp/favicon-32x32.png">
</head>
<body>
    <div id="redoc-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"></script>
    <script>
        Redoc.init(%s, {"hideHostname": true}, document.getElementById("redoc-container"));
    </script>
</body>
</html>"""
            % json.dumps(app.openapi())
        )
