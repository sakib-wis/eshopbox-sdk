Advanced Usage Examples
=======================

Webhook Registration
--------------------

.. code-block:: python

   response = sdk.webhooks.create({
       "event": "order.created",
       "callbackUrl": "https://yourapp.com/webhooks"
   })

Rate Calculator
---------------

.. code-block:: python

   rate = sdk.rate_calculator.calculate({
       "origin": "DEL",
       "destination": "MUM",
       "weight": 1.2
   })

Inventory Updates
-----------------

.. code-block:: python

   inventory = sdk.inventory.update_stock({
       "sku": "SKU001",
       "quantity": 15
   })
