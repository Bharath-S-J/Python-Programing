# Import the entire 'shipping' module from the 'ecommerce' package
import ecommerce.shipping

# Call the calc_shipping() function using the full module path
ecommerce.shipping.calc_shipping()
# Explanation:
# - Imports the entire 'shipping' module from the 'ecommerce' package.
# - Calls the 'calc_shipping()' function from the imported module using the full module path.

# Import only the 'calc_shipping()' function from the 'shipping' module within 'ecommerce'
from ecommerce.shipping import calc_shipping

# Call the calc_shipping() function directly
calc_shipping()
# Explanation:
# - Imports only the 'calc_shipping()' function from the 'shipping' module within 'ecommerce'.
# - Allows direct usage of the 'calc_shipping()' function without referencing the module name.

# Import the 'shipping' module from the 'ecommerce' package
from ecommerce import shipping

# Call the calc_shipping() function using the imported 'shipping' module
shipping.calc_shipping()
# Explanation:
# - Imports the 'shipping' module from the 'ecommerce' package.
# - Calls the 'calc_shipping()' function from the imported 'shipping' module.


