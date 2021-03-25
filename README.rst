
.. note::

    This project does **not** require any GIS library or specific database.
    Map data are stored in simple JSON fields.

Install
=======
clone de Repo

.. code-block:: bash

    git clone https://github.com/hyndruide/zerogachismap.git

Create a virtual environement

.. code-block:: bash

    cd zerogachismap
    python -m venv .
    // on linux
    source .venv/bin/activate
    // on windows
    .\venv\Scripts\Activate.ps1

Install Django dependencies:

.. code-block:: bash

    pip install -r requirements.txt

Initialize database tables:

.. code-block:: bash

    python manage.py migrate

Populate the database:

.. code-block:: bash

    python manage.py loaddata data.json

Create a super-user for the admin:

.. code-block:: bash

    python manage.py createsuperuser

Run
===

.. code-block:: bash

    python manage.py runserver

The map visible on http://127.0.0.1:8000/ can be edited from the AdminSite at ``/admin``.
