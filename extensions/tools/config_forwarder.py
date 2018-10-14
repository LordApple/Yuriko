from extensions.tools import default

owners = default.get("config.json").owners


def is_owner(ctx):
    return ctx.author.id in owners