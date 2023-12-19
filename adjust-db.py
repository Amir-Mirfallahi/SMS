from admin_interface.models import Theme


Theme.objects.raw(
    """INSERT INTO public.admin_interface_theme (
id, name, active, title, title_visible, logo, logo_visible, css_header_background_color, title_color, css_header_text_color, css_header_link_color, css_header_link_hover_color, css_module_background_color, css_module_text_color, css_module_link_color, css_module_link_hover_color, css_module_rounded_corners, css_generic_link_color, css_generic_link_hover_color, css_save_button_background_color, css_save_button_background_hover_color, css_save_button_text_color, css_delete_button_background_color, css_delete_button_background_hover_color, css_delete_button_text_color, list_filter_dropdown, related_modal_active, related_modal_background_color, related_modal_rounded_corners, logo_color, recent_actions_visible, favicon, related_modal_background_opacity, env_name, env_visible_in_header, env_color, env_visible_in_favicon, related_modal_close_button_visible, language_chooser_active, language_chooser_display, list_filter_sticky, form_pagination_sticky, form_submit_sticky, css_module_background_selected_color, css_module_link_selected_color, logo_max_height, logo_max_width, foldable_apps, language_chooser_control, list_filter_highlight, list_filter_removal_links, show_fieldsets_as_tabs, show_inlines_as_tabs, css_generic_link_active_color, collapsible_stacked_inlines, collapsible_stacked_inlines_collapsed, collapsible_tabular_inlines, collapsible_tabular_inlines_collapsed) VALUES(
    '2'::integer, 'اصلی'::character
varying, true::boolean, 'شهدای فرهنگی - پنل مدیریت'::character
varying, false::boolean, 'admin-interface/logo/logo_G7F9eto.png'::character
varying, true::boolean, '#112E51'::character
varying, '#FFFFFF'::character
varying, '#FFFFFF'::character
varying, '#FFFFFF'::character
varying, '#E1F3F8'::character
varying, '#205493'::character
varying, '#FFFFFF'::character
varying, '#FFFFFF'::character
varying, '#E1F3F8'::character
varying, true::boolean, '#205493'::character
varying, '#0071BC'::character
varying, '#205493'::character
varying, '#112E51'::character
varying, '#FFFFFF'::character
varying, '#CD2026'::character
varying, '#981B1E'::character
varying, '#FFFFFF'::character
varying, false::boolean, true::boolean, '#000000'::character
varying, true::boolean, '#FFFFFF'::character
varying, true::boolean, 'admin-interface/favicon/logo_63U9Lna.png'::character
varying, '0.8'::character
varying, 'شهدای فرهنگی'::character
varying, true::boolean, '#E74C3C'::character
varying, true::boolean, true::boolean, true::boolean, 'code'::character
varying, true::boolean, false::boolean, false::boolean, '#FFFFCC'::character
varying, '#FFFFFF'::character
varying, '100'::smallint, '100'::smallint, true::boolean, 'default-select'::character
varying, true::boolean, false::boolean, false::boolean, false::boolean, '#29B864'::character
varying, false::boolean, true::boolean, false::boolean, true::boolean)
returning
id;
""")
