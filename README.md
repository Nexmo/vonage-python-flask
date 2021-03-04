# Vonage Client Extension for Flask
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

<img src="https://developer.nexmo.com/assets/images/Vonage_Nexmo.svg" height="48px" alt="Nexmo is now known as Vonage" />

This is the Vonage API Python client extension for use with Flask.
To use this, you'll need a Vonage account. Sign up [for free at nexmo.com][signup].

**This bundle is currently in development/beta status, so there may be bugs**

 * [Installation](#installation)
 * [Usage](#usage)
 * [Contributing](#contributing) 

## Installation

For the lastest released version, you can install the extension using pip:

```console
$ pip install flask_vonage
```

If you would like the lasted development version, you can install directly from Github:

```console
$ pip install git+git+https://github.com/nexmo/vonage-python-flask=flask_vonage
```

### Configuration

This extension will pull configuration values from the Flask application config.

You can set the following configuration keys:

* `VONAGE_API_KEY` - Your Vonage API Key
* `VONAGE_API_SECRET` - Your Vonage API Secret
* `VONAGE_API_SIGNATURE_SECRET` - Your Vonage Signature secret for signed SMS
* `VONAGE_API_SIGNATURE_METHOD` - Signature hashing method from your Dashboard
* `VONAGE_APPLICATION_ID` - A Vonage Application ID
* `VONAGE_PRIVATE_KEY` - Path the the matching Application private key, or a string containing the private key

You can then fill in the needed credentials from your [Vonage Dashboard][dashboard].

```python
from flask import Flask
from flask_vonage import Vonage

app = Flask(__name__)
app.config.update(
    VONAGE_API_KEY="your_key",
    VONAGE_API_SECRET="your_secret"
)
vonage = Vonage(app)
```

## Usage

This bundle takes care of all the client creation needed for making the Vonage
client, and handles the boilerplate for accessing our APIs. All you need to do
is add your credentials and any other info like Vonage Application ID to your
config. You can pull then call the generated object and get the base client or
any associated API objects automatically.

```python
from flask import Flask
from flask_vonage import Vonage

app = Flask(__name__)
app.config.update(
    VONAGE_API_KEY="your_key",
    VONAGE_API_SECRET="your_secret"
)
vonage = Vonage(app)

@app.route("/")
def hello():
    res = vonage.sms.send_message({
        "from": "15556660001",
        "to": "155577700001",
        "text": "This was sent using the Vonage Flask extension"
    })
    print(res)
    return '', 204

if __name__ == "__main__":
    app.run()
```

[signup]: https://dashboard.nexmo.com/sign-up?utm_source=DEV_REL&utm_medium=github&utm_campaign=php-symfony-bundle
[dashboard]: https://dashboard.nexmo.com?utm_source=DEV_REL&utm_medium=github&utm_campaign=php-symfony-bundles
[issues]: https://github.com/nexmo/vonage-python-flask/issues
[pulls]: https://github.com/nexmo/vonage-python-flask/pulls



## Contributing

We ❤️ contributions from everyone! [Bug reports](https://github.com/nexmo/vonage-python-flask/issues), [bug fixes](https://github.com/nexmo/vonage-python-flask/pulls) and feedback on the application is always appreciated. Look at the [Contributor Guidelines](https://github.com/nexmo/vonage-python-flask/blob/master/CONTRIBUTING.md) for more information and please follow the [GitHub Flow](https://guides.github.com/introduction/flow/index.html).

## License

This projet is under the [MIT License](LICENSE)