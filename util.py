from dataclasses import dataclass


@dataclass
class LightningDocs:
    version: str


@dataclass
class Knackly:
    tenancy: str
    keyID: str
    secret: str
    catalog_name: str
    app_name: str
    refresh_token: str


@dataclass
class Config:
    """Class for setting up a configuration to be used in the Jupyter Notebook."""

    lightningdocs: LightningDocs
    knackly: Knackly


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
    print(
        "{}\n{}\r\n{}\r\n\r\n{}".format(
            "-----------START-----------",
            req.method + " " + req.url,
            "\r\n".join("{}: {}".format(k, v) for k, v in req.headers.items()),
            req.body,
        )
    )
