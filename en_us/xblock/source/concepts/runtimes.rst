.. _XBlock Runtimes:

####################
XBlock Runtimes
####################

An XBlock runtime is the application that hosts XBlock. For example, the XBlock
SDK, the :ref:`edX LMS <EdX Learning Management System as an XBlock Runtime>`,
and :ref:`edX Studio <EdX Studio as an XBlock Runtime>` are all XBlock runtime
applications.
   
.. contents::
 :local:
 :depth: 1

******************
Runtime Functions
******************

An XBlock runtime application must perform the following functions.

* Instantiate XBlocks with the correct data access.
  
* Display the HTML returned by XBlock views.
  
  .. note:: 
    Runtime applications must document the view names they require of XBlocks.
  
* Bind the front-end JavaScript code to the correct DOM elements.
  
* Route handler requests from the client-side XBlock to the server-side
  handlers.

******************
Extending XBlocks
******************

When constructing a runtime instance, a runtime application can provide a list
of mixin classes. These classes are used whenever the runtime constructs an
XBlock to generate a new subclass of that XBlock with the mixins added as base
classes. This allows a runtime application to add field data and methods to all
XBlocks that it hosts, without requiring that XBlocks themselves are
aware of the runtime they are being hosted in.

***********************
Creating a new Runtime
***********************

A new XBlock runtime must provide the following capabilities.

* Access to external resources and is responsible for constructing XBlocks.

* A ``FieldData`` implementation, which provides access the underlying data
  storage for the XBlock fields.

* A ``UsageStore``, which provides mappings between the various
  fields of Scope IDs. [KEEP? STILL PROPOSED?]

* Access to XBlock views and handlers.

================
Rendering Views
================

A runtime application must document which XBlock views it renders, and in what
context it will render those views. XBlock developers write views with those
specific names so that they interact properly with the runtime application.

When a runtime renders a view by calling ``Runtime.render()`` or
``XBlock.render()``, it receives a Fragment as a result.

The runtime must embed ``Fragment.content`` into the HTML it is producing, add
``Fragment.head_html()`` to the head of the page, and add
``Fragment.foot_html()`` to the foot of the page. This ensures that the
JavaScript and CSS for all of the fragments on the page are combined properly.

================
Routing Handlers
================

A runtime application routes requests from the client-side XBlock to the
server-side XBlock handler functions. The runtime’s implementation of
``Runtime.handler_url()`` must return a relative URL that the client-side
XBlock can call to pass data back to the server.

Authentication of the handler is managed by the runtime application, although
you can also request a URL that is unauthenticated for use from third-party
applications.

XBlock implementations might have arbitrarily named handler functions, so the
runtime application must be able to route to any of them.

********************
JavaScript Runtimes
********************

The application that runs XBlocks uses a JavaScript runtime to load XBlocks.
Specifically, the JavaScript runtime provides the following functions to
XBlocks.

* The Runtime Handler

* XBlock Children

* A map of the XBlock children

==================================
The XBlock SDK JavaScript Runtime
==================================

The file `1.js`_ in the XBlock SDK provides the JavaScript runtime for the
workbench.

.. include:: ../reusable/code_javascript_runtime.rst

==============================
The JavaScript Runtime Handler
==============================

The JavaScript runtime initializes the XBlock each time it is loaded by a user
and returns the handler so the XBlock can communicate with the server.

From the example above, the following part of the runtime generates and returns
the handler to the XBlock.

.. code-block:: javascript

    var versions = {
      1: {
        handlerUrl: function(block, handlerName, suffix, query) {
          suffix = typeof suffix !== 'undefined' ? suffix : '';
          query = typeof query !== 'undefined' ? query : '';
          var usage = $(block).data('usage');
          var url_selector = $(block).data('url_selector');
          if (url_selector !== undefined) {
            baseUrl = window[url_selector];
          }
          else {baseUrl = handlerBaseUrl;}

          // studentId and handlerBaseUrl are both defined in block.html
          return (baseUrl + usage +
                           "/" + handlerName +
                           "/" + suffix +
                   "?student=" + studentId +
                           "&" + query);
        . . .

The runtime handler code is called by the XBlock’s JavaScript code to get the
XBlock URL.

For example, the `Thumbs XBlock`_ in the XBlock SDK, the `thumbs.js`_ file gets
the handler from the XBlock runtime.

.. code-block:: javascript

    var handlerUrl = runtime.handlerUrl(element, 'vote');

================
XBlock Children
================

The JavaScript runtime also returns the list of child XBlocks to the XBlock.

From the example above, the following part of the runtime returns the list of
children to the XBlock.

.. code-block:: javascript

    . . .

    children: function(block) {
      return $(block).prop('xblock_children');
    },
    . . .

An XBlock uses the ``children`` method when it needs to iterate over an ordered
list of its child XBlocks.

=================
XBlock Child Map
=================

The JavaScript runtime also returns the a map of child XBlocks to the running
XBlock.

From the example above, the following part of the runtime generates and returns
the list of children to the XBlock.

.. code-block:: javascript

    . . .

    childMap: function(block, childName) {
        var children = this.children(block);
        for (var i = 0; i < children.length; i++) {
            var child = children[i];
            if (child.name == childName) {
                return child
            }
        }
    }
    . . .

An XBlock uses the ``childMap`` function when it needs to access different
child XBlocks to perform different actions on them.

For example, the `Problem XBlock`_ in the XBlock SDK loads JavaScript code that
gets the map of child XBlocks.

.. code-block:: javascript

    function handleCheckResults(results) {
    $.each(results.submitResults || {}, function(input, result) {
         callIfExists(runtime.childMap(element, input), 'handleSubmit', result);
     });
    $.each(results.checkResults || {}, function(checker, result) {
        callIfExists(runtime.childMap(element, checker), 'handleCheck', result);

******************
XBlock Runtime API
******************

.. links to api doc

.. include:: ../links.rst