import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import (conc_twtags,
                               tstr,
                               pd,
                               grow,
                               bg,
                               green,
                               W,
                               fc,
                               gray,
                               space,
                               y,
                               mr,
                               st,
                               srs,
                               ta)

from html_writer.macro_module import macros, writer_ctx

def GridUSP():
    
    with writer_ctx:
        with Section(classes='bg-gray-900 text-white') as comp_box:
            with Div(classes='max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16'):
                with Div(classes='max-w-xl'):
                    with H2(classes='text-3xl font-bold sm:text-4xl', text="What makes us special"):
                        pass
                        

                    with P(classes='mt-4 text-gray-300', text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat dolores iure fugit totam iste obcaecati. Consequatur ipsa quod ipsum sequi culpa delectus, cumque id tenetur quibusdam, quos fuga minima."):
                        pass
                        
                    pass
                
                with Div(classes='mt-8 grid grid-cols-1 gap-8 md:mt-16 md:grid-cols-2 md:gap-12 lg:grid-cols-3'):
                    with Div(classes='flex items-start gap-4'):
                        with Span(classes="shrink-0 rounded-lg bg-gray-800 p-4"):
                            with FontAwesomeIcon(label="faGraduationSchool",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="school",
                                         classes="w-5 h-5",
                            
                                 ):
                                pass

                        with Div():
                            with H2(classes='text-lg font-bold', text="Technology Solutions:"):
                                pass


                            with P(classes='mt-1 text-sm text-gray-300', text="A leader in cutting-edge technology solutions, providing innovative software and hardware solutions for businesses of all sizes. Our team of experts specializes in developing custom software, implementing scalable infrastructure, and leveraging emerging technologies to drive digital transformation"):
                                pass

    return comp_box                        
def demo_testimonial(idx):
    with writer_ctx:
        with Div(classes='-mx-6 lg:col-span-2 lg:mx-0') as root_box:
            with Div(classes='', id='keen-slider'):
                with Div(classes=''):
                    with Div(
                        classes='flex h-full flex-col justify-between bg-white p-6 shadow-sm sm:p-8 lg:p-12'
                    ):
                        with Div():
                            with Div(classes='flex gap-0.5 text-green-500'):
                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass

                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass

                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass

                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass

                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass

                                with FontAwesomeIcon(label="faStar",
                                         size="1x", 
                                         fixedWidth=True,
                                         fa_group="regular",
                                         mdi_label="star",
                                         classes="w-5 h-5",
                            
                                 ):
                                    pass                                            



                            with Div(classes='mt-4'):
                                with P(classes='text-2xl font-bold text-rose-600 sm:text-3xl', text=f"Stayin' Alive"):
                                    pass

                                with P(classes='mt-4 leading-relaxed text-gray-700' , text="No, Rose, they are not breathing. And they have no arms or legs … Where are they? You know what? If we come across somebody with no arms or legs, do we bother resuscitating them? I mean, what quality of life do we have there?"):
                                    pass


                        with Footer(classes='mt-4 text-sm font-medium text-gray-700 sm:mt-6', text=f"Review item {idx}"):
                            pass


    return root_box
