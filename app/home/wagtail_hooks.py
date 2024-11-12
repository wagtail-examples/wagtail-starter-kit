from wagtail import hooks

# Adjust the font size in the <wagtail-userbar>
# on larger screens so the text doesn't wrap.
# The problem is the --pico-font-size leaks
# into the userbar and increases the font size.
userbar_fix = """
    <style>
    @media (min-width: 576px) {
        .w-userbar__item a { font-size: 0.8rem; }
    }
    @media (min-width: 1536px) {
        .w-userbar__item a { font-size: 0.75rem; }
    }
    </style>
"""


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return userbar_fix
