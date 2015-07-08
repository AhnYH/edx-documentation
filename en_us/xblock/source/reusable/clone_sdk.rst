********************************************
Install the XBlock Software Development Kit
********************************************

After you :ref:`create and activate the virtual environment <Create and
Activate the Virtual Environment>`, you install the `XBlock SDK`_ and its
requirements. To do this, complete the following steps at a command prompt.

#. In the ``xblock_development`` directory, run the following command to clone
   the XBlock SDK repository from GitHub.

   .. code-block:: bash

      (venv) $ git clone https://github.com/edx/xblock-sdk.git

#. When the XBlock SDK is cloned, run the following command to go to the
   ``xblock-sdk`` directory in the virtual environment.

   .. code-block:: bash

      (venv) $ cd xblock-sdk

#. From the ``xblock-sdk`` directory, run the following command to install the
   XBlock SDK requirements.

   .. code-block:: bash
  
      (venv) $ pip install -r requirements.txt
