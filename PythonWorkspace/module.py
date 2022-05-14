# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv  # USE mv -> theater_module
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


from theater_module import *
# ex from random import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price_soldier as price  ##IMPORTANT##
price(5)
