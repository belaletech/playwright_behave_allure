def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
