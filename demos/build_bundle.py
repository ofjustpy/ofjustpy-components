import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

twtags, fontawesome_icons = get_svelte_safelist("demo_mouseover_slideshow")

use_shadcn = True
use_skeleton = True

# which components and themes to include
skeleton_config = { 'components': [],
                    'themes': [],

    }

# which font families to include
font_families = ["Geist", "Roboto"]

from  svelte_bundler import hyperui_bundle_builder


hyperui_bundle_builder.build_bundle(twtags,
                            font_families=font_families,
                            fontawesome_icons = fontawesome_icons,
                            output_dir="./static/hyperui"
                            )


