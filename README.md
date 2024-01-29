# A Simple Calculator Flet App

An example of a minimal Flet app which is a fork (with minimal modification) from [this calculator app](https://github.com/taaaf11/Calculator).


To run the app:

```shell
flet run
```

## Deploy

- **Web App** currently deployed via [Netlify](https://flet-calculator-lightbridge.netlify.app/)
- **Desktop App** in the [release section](https://github.com/Lightbridge-KS/flet-calculator/releases) build by appveyor

## Hard lesson in `requirements.txt`

<https://flet.dev/docs/guides/python/packaging-app-for-distribution/#native-python-packages>

In `requirements.txt` do not include other package that depend on other languages.

I've used this config and fail:

```text
pyinstaller>=5.7.0
pillow==10.2.0
```

Using just `flet` works fine.