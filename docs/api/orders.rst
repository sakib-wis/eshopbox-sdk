Orders API
==========

.. module:: eshopbox.api.orders
   :synopsis: Order management operations for the EShopBox API.

Overview
--------

The ``OrdersAPI`` class provides methods to interact with order resources in
the EShopBox platform. It allows you to retrieve, create, cancel, and fetch
invoice details for orders.

This module inherits from :class:`eshopbox.api.base.BaseAPI`.

Class: OrdersAPI
----------------

.. class:: OrdersAPI(workspace, auth)

   Handle all order-related operations.

   **Parameters**

   - ``workspace`` (*str*) – Your EShopBox workspace name.
   - ``auth`` (*EShopBoxAuth*) – Authentication handler for generating tokens.

   **Example**

   .. code-block:: python

      from eshopbox import EShopBoxSDK

      sdk = EShopBoxSDK(
          workspace="myshop",
          client_id="CLIENT_ID",
          client_secret="SECRET",
          refresh_token="REFRESH"
      )

      orders = sdk.orders.get_all()

Methods
-------

get_all
~~~~~~~

.. method:: OrdersAPI.get_all(page=1, **filters)

   Retrieve all orders with optional filters.

   **Parameters**

   - ``page`` (*int*, default=1) – Page number for pagination.
   - ``**filters`` – Any additional query filters.

   **Returns**

   - ``dict`` – Response containing paginated order data.

   **Example**

   .. code-block:: python

      response = sdk.orders.get_all(page=2, status="SHIPPED")

get
~~~

.. method:: OrdersAPI.get(customer_order_number)

   Fetch a specific order by its customer order number.

   **Parameters**

   - ``customer_order_number`` (*str*) – Unique identifier of the order.

   **Returns**

   - ``dict`` – Order details.

   **Example**

   .. code-block:: python

      order = sdk.orders.get("ORD12345")

create
~~~~~~

.. method:: OrdersAPI.create(order_data)

   Create a new order.

   **Parameters**

   - ``order_data`` (*dict*) – Full order structure including items, customer
     details, addresses, and channel information.

   **Returns**

   - ``dict`` – Created order details.

   **Example**

   .. code-block:: python

      payload = {
         "externalChannelID": "CH1234",
         "customerOrderNumber": "ORD123",
         "items": [],
         "shippingAddress": {}
      }

      created = sdk.orders.create(payload)

cancel
~~~~~~

.. method:: OrdersAPI.cancel(cancel_data)

   Cancel an existing order.

   **Parameters**

   - ``cancel_data`` (*dict*) – Cancellation info including order number and reason.

   **Returns**

   - ``dict`` – Confirmation response.

   **Example**

   .. code-block:: python

      data = {
         "customerOrderNumber": "ORD123",
         "reason": "Customer request"
      }

      result = sdk.orders.cancel(data)

get_invoice
~~~~~~~~~~~

.. method:: OrdersAPI.get_invoice(order_number)

   Retrieve invoice details for a specific order.

   **Parameters**

   - ``order_number`` (*str*) – Order number.

   **Returns**

   - ``dict`` – Invoice information.

   **Example**

   .. code-block:: python

      invoice = sdk.orders.get_invoice("ORD123")
