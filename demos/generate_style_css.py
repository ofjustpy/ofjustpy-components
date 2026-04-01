from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css
#target_module = "td_color_shade_selector"
#target_module = "td_linear_selector"
#target_module = "demo_two_column_stackv"
target_module = "demo_var_length_list"
build_ssr_style_css(target_module,
                    output_dir="./static/ssr/",
                    
                    )
