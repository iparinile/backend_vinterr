from .base import BaseEndpoint
from .helth import HealthEndpoint

from .users.create import CreateUserEndpoint
from .users.auth import AuthUserEndpoint
from .users.user import UserEndpoint

from .customers.create import CreateCustomerEndpoint
from .customers.auth import AuthCustomerEndpoint
from .customers.customer import CustomerEndpoint

from .materials.create import CreateMaterialEndpoint
from .materials.material import MaterialEndpoint
from .materials.get_all import GetAllMaterialsEndpoint

from .categories.category import CategoryEndpoint
from .categories.create import CreateCategoryEndpoint
from .categories.get_all import GetAllCategoriesEndpoint

from .structures.structure import StructureEndpoint
from .structures.create import CreateStructureEndpoint
from .structures.get_all import GetAllStructuresEndpoint

from .sizes.size import SizeEndpoint
from .sizes.create import CreateSizeEndpoint
from .sizes.get_all import GetAllSizesEndpoint

from .statuses.status import StatusEndpoint
from .statuses.create import CreateStatusEndpoint
from .statuses.get_all import GetAllStatusesEndpoint

from .colors.color import ColorEndpoint
from .colors.create import CreateColorEndpoint
from .colors.get_all import GetAllColorsEndpoint

from .goods.create import CreateGoodEndpoint
from .goods.get_all import GetAllGoodsEndpoint
from .goods.get_variations import GetVariationsForGoodEndpoint
from .goods.good import GoodEndpoint

from .variations.create import CreateVariationEndpoint
from .variations.get_all import GetAllVariationsEndpoint
from .variations.get_variation import GetVariationEndpoint
from .variations.variation import VariationEndpoint
from .variations.update_remains import UpdateRemainsEndpoint

from .images.image import ImageEndpoint
from .images.create import CreateImageEndpoint

from .orders.create import CreateOrderEndpoint
from .orders.get_all import GetAllOrdersEndpoint
from .orders.order import OrderEndpoint

from .contact_forms.create import CreateContactFormEndpoint

from .delivery_types.create import CreateDeliveryTypeEndpoint
from .delivery_types.get_all import GetAllDeliveryTypesEndpoint
from .delivery_types.delivery_type import DeliveryTypeEndpoint

from .payments.register import RegisterPaymentsEndpoint
from .payments.get_status import GetStatusPaymentsEndpoint

from .telegram_users.create import CreateTelegramUserEndpoint
from .telegram_users.telegram_user import TelegramUserEndpoint

from .status_changes.get_all_for_order import GetAllStatusChangesForOrderEndpoint
from .status_changes.get_all import GetAllStatusChangesEndpoint

from .products_care.products_care import ProductsCareEndpoint
from .products_care.create import CreateProductsCareEndpoint
from .products_care.get_all import GetAllProductsCareEndpoint
