from flask import Flask, render_template

app = Flask(__name__)

NAV_ITEMS = [
    {"endpoint": "home", "label": "Головна"},
    {"endpoint": "html_tags", "label": "HTML"},
    {"endpoint": "css_selectors", "label": "CSS"},
    {"endpoint": "css_units", "label": "Одиниці розміру"},
    {"endpoint": "css_layout", "label": "Розміщення блоків"},
    {"endpoint": "css_position", "label": "Position"},
    {"endpoint": "css_position_demo", "label": "Демо Position"},
    {"endpoint": "css_animations", "label": "Анімації"},
    {"endpoint": "css_animations_demo", "label": "Демо Анімацій"},
    {"endpoint": "connect_css", "label": "Підключення CSS"},
    {"endpoint": "flask_basics", "label": "Flask"},
    {"endpoint": "flask_forms", "label": "Форми"},
    {"endpoint": "jinja_templates", "label": "Шаблони Jinja"},
]

PAGES = [
    {"rule": "/", "legacy_rule": "/index.html", "endpoint": "home", "template": "pages/index.html", "active_page": "home"},
    {"rule": "/html-tags", "legacy_rule": "/html-tags.html", "endpoint": "html_tags", "template": "pages/html-tags.html", "active_page": "html_tags"},
    {"rule": "/css-selectors", "legacy_rule": "/css-selectors.html", "endpoint": "css_selectors", "template": "pages/css-selectors.html", "active_page": "css_selectors"},
    {"rule": "/css-units", "legacy_rule": "/css-units.html", "endpoint": "css_units", "template": "pages/css-units.html", "active_page": "css_units"},
    {"rule": "/css-layout", "legacy_rule": "/css-layout.html", "endpoint": "css_layout", "template": "pages/css-layout.html", "active_page": "css_layout"},
    {"rule": "/css-position", "legacy_rule": "/css-position.html", "endpoint": "css_position", "template": "pages/css-position.html", "active_page": "css_position"},
    {"rule": "/css-position-demo", "legacy_rule": "/css-position-demo.html", "endpoint": "css_position_demo", "template": "pages/css-position-demo.html", "active_page": "css_position_demo"},
    {"rule": "/css-animations", "legacy_rule": "/css-animations.html", "endpoint": "css_animations", "template": "pages/css-animations.html", "active_page": "css_animations"},
    {"rule": "/css-animations-demo", "legacy_rule": "/css-animations-demo.html", "endpoint": "css_animations_demo", "template": "pages/css-animations-demo.html", "active_page": "css_animations_demo"},
    {"rule": "/connect-css", "legacy_rule": "/connect-css.html", "endpoint": "connect_css", "template": "pages/connect-css.html", "active_page": "connect_css"},
    {"rule": "/flask-basics", "legacy_rule": "/flask-basics.html", "endpoint": "flask_basics", "template": "pages/flask-basics.html", "active_page": "flask_basics"},
    {"rule": "/flask-forms", "legacy_rule": "/flask-forms.html", "endpoint": "flask_forms", "template": "pages/flask-forms.html", "active_page": "flask_forms"},
    {"rule": "/jinja-templates", "legacy_rule": "/jinja-templates.html", "endpoint": "jinja_templates", "template": "pages/jinja-templates.html", "active_page": "jinja_templates"},
]


def render_page(template_name: str, active_page: str):
    return render_template(
        template_name,
        nav_items=NAV_ITEMS,
        active_page=active_page,
    )


def make_view(template_name: str, active_page: str):
    def view():
        return render_page(template_name, active_page)

    return view


for page in PAGES:
    app.add_url_rule(
        page["rule"],
        endpoint=page["endpoint"],
        view_func=make_view(page["template"], page["active_page"]),
    )
    app.add_url_rule(
        page["legacy_rule"],
        endpoint=f"{page['endpoint']}_legacy",
        view_func=make_view(page["template"], page["active_page"]),
    )


if __name__ == "__main__":
    app.run(debug=True)
