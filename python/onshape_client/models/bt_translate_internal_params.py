# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.97
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTTranslateInternalParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'model_scope': 'BTDocumentScope',
        'notify_user': 'bool',
        'part_ids': 'str',
        'connection_id': 'str',
        'store_in_document': 'bool',
        'from_user_id': 'str',
        'cloud_storage_account_id': 'str',
        'cloud_object_id': 'str',
        'email_link': 'bool',
        'email_subject': 'str',
        'email_message': 'str',
        'email_to': 'list[str]',
        'send_copy_to_me': 'bool',
        'trigger_auto_download': 'bool',
        'format_name': 'str',
        'version_string': 'str',
        'source_name': 'str',
        'destination_name': 'str',
        'text_as_geometry': 'bool',
        'flatten': 'bool',
        'include_export_ids': 'bool',
        'show_overridden_dimensions': 'bool',
        'current_sheet_only': 'bool',
        'image_width': 'int',
        'image_height': 'int',
        'color_method': 'str',
        'splines_as_polylines': 'bool',
        'selectable_pdf_text': 'bool',
        'grouping': 'bool',
        'import_in_background': 'bool',
        'project_id': 'str',
        'parent_id': 'str',
        'foreign_id': 'str',
        'upload_id': 'str',
        'specify_units': 'bool',
        'unit': 'str',
        'original_foreign_id': 'str',
        'import_within_document': 'bool',
        'blob_element_id': 'str',
        'blob_microversion_id': 'str',
        'split_assemblies_into_multiple_documents': 'bool',
        'flatten_assemblies': 'bool',
        'gety_axis_is_up': 'bool',
        'allow_faulty_parts': 'bool'
    }

    attribute_map = {
        'model_scope': 'modelScope',
        'notify_user': 'notifyUser',
        'part_ids': 'partIds',
        'connection_id': 'connectionId',
        'store_in_document': 'storeInDocument',
        'from_user_id': 'fromUserId',
        'cloud_storage_account_id': 'cloudStorageAccountId',
        'cloud_object_id': 'cloudObjectId',
        'email_link': 'emailLink',
        'email_subject': 'emailSubject',
        'email_message': 'emailMessage',
        'email_to': 'emailTo',
        'send_copy_to_me': 'sendCopyToMe',
        'trigger_auto_download': 'triggerAutoDownload',
        'format_name': 'formatName',
        'version_string': 'versionString',
        'source_name': 'sourceName',
        'destination_name': 'destinationName',
        'text_as_geometry': 'textAsGeometry',
        'flatten': 'flatten',
        'include_export_ids': 'includeExportIds',
        'show_overridden_dimensions': 'showOverriddenDimensions',
        'current_sheet_only': 'currentSheetOnly',
        'image_width': 'imageWidth',
        'image_height': 'imageHeight',
        'color_method': 'colorMethod',
        'splines_as_polylines': 'splinesAsPolylines',
        'selectable_pdf_text': 'selectablePdfText',
        'grouping': 'grouping',
        'import_in_background': 'importInBackground',
        'project_id': 'projectId',
        'parent_id': 'parentId',
        'foreign_id': 'foreignId',
        'upload_id': 'uploadId',
        'specify_units': 'specifyUnits',
        'unit': 'unit',
        'original_foreign_id': 'originalForeignId',
        'import_within_document': 'importWithinDocument',
        'blob_element_id': 'blobElementId',
        'blob_microversion_id': 'blobMicroversionId',
        'split_assemblies_into_multiple_documents': 'splitAssembliesIntoMultipleDocuments',
        'flatten_assemblies': 'flattenAssemblies',
        'gety_axis_is_up': 'getyAxisIsUp',
        'allow_faulty_parts': 'allowFaultyParts'
    }

    def __init__(self, model_scope=None, notify_user=None, part_ids=None, connection_id=None, store_in_document=None, from_user_id=None, cloud_storage_account_id=None, cloud_object_id=None, email_link=None, email_subject=None, email_message=None, email_to=None, send_copy_to_me=None, trigger_auto_download=None, format_name=None, version_string=None, source_name=None, destination_name=None, text_as_geometry=None, flatten=None, include_export_ids=None, show_overridden_dimensions=None, current_sheet_only=None, image_width=None, image_height=None, color_method=None, splines_as_polylines=None, selectable_pdf_text=None, grouping=None, import_in_background=None, project_id=None, parent_id=None, foreign_id=None, upload_id=None, specify_units=None, unit=None, original_foreign_id=None, import_within_document=None, blob_element_id=None, blob_microversion_id=None, split_assemblies_into_multiple_documents=None, flatten_assemblies=None, gety_axis_is_up=None, allow_faulty_parts=None):  # noqa: E501
        """BTTranslateInternalParams - a model defined in OpenAPI"""  # noqa: E501

        self._model_scope = None
        self._notify_user = None
        self._part_ids = None
        self._connection_id = None
        self._store_in_document = None
        self._from_user_id = None
        self._cloud_storage_account_id = None
        self._cloud_object_id = None
        self._email_link = None
        self._email_subject = None
        self._email_message = None
        self._email_to = None
        self._send_copy_to_me = None
        self._trigger_auto_download = None
        self._format_name = None
        self._version_string = None
        self._source_name = None
        self._destination_name = None
        self._text_as_geometry = None
        self._flatten = None
        self._include_export_ids = None
        self._show_overridden_dimensions = None
        self._current_sheet_only = None
        self._image_width = None
        self._image_height = None
        self._color_method = None
        self._splines_as_polylines = None
        self._selectable_pdf_text = None
        self._grouping = None
        self._import_in_background = None
        self._project_id = None
        self._parent_id = None
        self._foreign_id = None
        self._upload_id = None
        self._specify_units = None
        self._unit = None
        self._original_foreign_id = None
        self._import_within_document = None
        self._blob_element_id = None
        self._blob_microversion_id = None
        self._split_assemblies_into_multiple_documents = None
        self._flatten_assemblies = None
        self._gety_axis_is_up = None
        self._allow_faulty_parts = None
        self.discriminator = None

        if model_scope is not None:
            self.model_scope = model_scope
        if notify_user is not None:
            self.notify_user = notify_user
        if part_ids is not None:
            self.part_ids = part_ids
        if connection_id is not None:
            self.connection_id = connection_id
        if store_in_document is not None:
            self.store_in_document = store_in_document
        if from_user_id is not None:
            self.from_user_id = from_user_id
        if cloud_storage_account_id is not None:
            self.cloud_storage_account_id = cloud_storage_account_id
        if cloud_object_id is not None:
            self.cloud_object_id = cloud_object_id
        if email_link is not None:
            self.email_link = email_link
        if email_subject is not None:
            self.email_subject = email_subject
        if email_message is not None:
            self.email_message = email_message
        if email_to is not None:
            self.email_to = email_to
        if send_copy_to_me is not None:
            self.send_copy_to_me = send_copy_to_me
        if trigger_auto_download is not None:
            self.trigger_auto_download = trigger_auto_download
        if format_name is not None:
            self.format_name = format_name
        if version_string is not None:
            self.version_string = version_string
        if source_name is not None:
            self.source_name = source_name
        if destination_name is not None:
            self.destination_name = destination_name
        if text_as_geometry is not None:
            self.text_as_geometry = text_as_geometry
        if flatten is not None:
            self.flatten = flatten
        if include_export_ids is not None:
            self.include_export_ids = include_export_ids
        if show_overridden_dimensions is not None:
            self.show_overridden_dimensions = show_overridden_dimensions
        if current_sheet_only is not None:
            self.current_sheet_only = current_sheet_only
        if image_width is not None:
            self.image_width = image_width
        if image_height is not None:
            self.image_height = image_height
        if color_method is not None:
            self.color_method = color_method
        if splines_as_polylines is not None:
            self.splines_as_polylines = splines_as_polylines
        if selectable_pdf_text is not None:
            self.selectable_pdf_text = selectable_pdf_text
        if grouping is not None:
            self.grouping = grouping
        if import_in_background is not None:
            self.import_in_background = import_in_background
        if project_id is not None:
            self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id
        if foreign_id is not None:
            self.foreign_id = foreign_id
        if upload_id is not None:
            self.upload_id = upload_id
        if specify_units is not None:
            self.specify_units = specify_units
        if unit is not None:
            self.unit = unit
        if original_foreign_id is not None:
            self.original_foreign_id = original_foreign_id
        if import_within_document is not None:
            self.import_within_document = import_within_document
        if blob_element_id is not None:
            self.blob_element_id = blob_element_id
        if blob_microversion_id is not None:
            self.blob_microversion_id = blob_microversion_id
        if split_assemblies_into_multiple_documents is not None:
            self.split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents
        if flatten_assemblies is not None:
            self.flatten_assemblies = flatten_assemblies
        if gety_axis_is_up is not None:
            self.gety_axis_is_up = gety_axis_is_up
        if allow_faulty_parts is not None:
            self.allow_faulty_parts = allow_faulty_parts

    @property
    def model_scope(self):
        """Gets the model_scope of this BTTranslateInternalParams.  # noqa: E501


        :return: The model_scope of this BTTranslateInternalParams.  # noqa: E501
        :rtype: BTDocumentScope
        """
        return self._model_scope

    @model_scope.setter
    def model_scope(self, model_scope):
        """Sets the model_scope of this BTTranslateInternalParams.


        :param model_scope: The model_scope of this BTTranslateInternalParams.  # noqa: E501
        :type: BTDocumentScope
        """

        self._model_scope = model_scope

    @property
    def notify_user(self):
        """Gets the notify_user of this BTTranslateInternalParams.  # noqa: E501


        :return: The notify_user of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._notify_user

    @notify_user.setter
    def notify_user(self, notify_user):
        """Sets the notify_user of this BTTranslateInternalParams.


        :param notify_user: The notify_user of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._notify_user = notify_user

    @property
    def part_ids(self):
        """Gets the part_ids of this BTTranslateInternalParams.  # noqa: E501


        :return: The part_ids of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._part_ids

    @part_ids.setter
    def part_ids(self, part_ids):
        """Sets the part_ids of this BTTranslateInternalParams.


        :param part_ids: The part_ids of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._part_ids = part_ids

    @property
    def connection_id(self):
        """Gets the connection_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The connection_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this BTTranslateInternalParams.


        :param connection_id: The connection_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def store_in_document(self):
        """Gets the store_in_document of this BTTranslateInternalParams.  # noqa: E501


        :return: The store_in_document of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._store_in_document

    @store_in_document.setter
    def store_in_document(self, store_in_document):
        """Sets the store_in_document of this BTTranslateInternalParams.


        :param store_in_document: The store_in_document of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._store_in_document = store_in_document

    @property
    def from_user_id(self):
        """Gets the from_user_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The from_user_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, from_user_id):
        """Sets the from_user_id of this BTTranslateInternalParams.


        :param from_user_id: The from_user_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._from_user_id = from_user_id

    @property
    def cloud_storage_account_id(self):
        """Gets the cloud_storage_account_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The cloud_storage_account_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._cloud_storage_account_id

    @cloud_storage_account_id.setter
    def cloud_storage_account_id(self, cloud_storage_account_id):
        """Sets the cloud_storage_account_id of this BTTranslateInternalParams.


        :param cloud_storage_account_id: The cloud_storage_account_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._cloud_storage_account_id = cloud_storage_account_id

    @property
    def cloud_object_id(self):
        """Gets the cloud_object_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The cloud_object_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._cloud_object_id

    @cloud_object_id.setter
    def cloud_object_id(self, cloud_object_id):
        """Sets the cloud_object_id of this BTTranslateInternalParams.


        :param cloud_object_id: The cloud_object_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._cloud_object_id = cloud_object_id

    @property
    def email_link(self):
        """Gets the email_link of this BTTranslateInternalParams.  # noqa: E501


        :return: The email_link of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._email_link

    @email_link.setter
    def email_link(self, email_link):
        """Sets the email_link of this BTTranslateInternalParams.


        :param email_link: The email_link of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._email_link = email_link

    @property
    def email_subject(self):
        """Gets the email_subject of this BTTranslateInternalParams.  # noqa: E501


        :return: The email_subject of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this BTTranslateInternalParams.


        :param email_subject: The email_subject of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

    @property
    def email_message(self):
        """Gets the email_message of this BTTranslateInternalParams.  # noqa: E501


        :return: The email_message of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._email_message

    @email_message.setter
    def email_message(self, email_message):
        """Sets the email_message of this BTTranslateInternalParams.


        :param email_message: The email_message of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._email_message = email_message

    @property
    def email_to(self):
        """Gets the email_to of this BTTranslateInternalParams.  # noqa: E501


        :return: The email_to of this BTTranslateInternalParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        """Sets the email_to of this BTTranslateInternalParams.


        :param email_to: The email_to of this BTTranslateInternalParams.  # noqa: E501
        :type: list[str]
        """

        self._email_to = email_to

    @property
    def send_copy_to_me(self):
        """Gets the send_copy_to_me of this BTTranslateInternalParams.  # noqa: E501


        :return: The send_copy_to_me of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._send_copy_to_me

    @send_copy_to_me.setter
    def send_copy_to_me(self, send_copy_to_me):
        """Sets the send_copy_to_me of this BTTranslateInternalParams.


        :param send_copy_to_me: The send_copy_to_me of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._send_copy_to_me = send_copy_to_me

    @property
    def trigger_auto_download(self):
        """Gets the trigger_auto_download of this BTTranslateInternalParams.  # noqa: E501


        :return: The trigger_auto_download of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._trigger_auto_download

    @trigger_auto_download.setter
    def trigger_auto_download(self, trigger_auto_download):
        """Sets the trigger_auto_download of this BTTranslateInternalParams.


        :param trigger_auto_download: The trigger_auto_download of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._trigger_auto_download = trigger_auto_download

    @property
    def format_name(self):
        """Gets the format_name of this BTTranslateInternalParams.  # noqa: E501


        :return: The format_name of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._format_name

    @format_name.setter
    def format_name(self, format_name):
        """Sets the format_name of this BTTranslateInternalParams.


        :param format_name: The format_name of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._format_name = format_name

    @property
    def version_string(self):
        """Gets the version_string of this BTTranslateInternalParams.  # noqa: E501


        :return: The version_string of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._version_string

    @version_string.setter
    def version_string(self, version_string):
        """Sets the version_string of this BTTranslateInternalParams.


        :param version_string: The version_string of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._version_string = version_string

    @property
    def source_name(self):
        """Gets the source_name of this BTTranslateInternalParams.  # noqa: E501


        :return: The source_name of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this BTTranslateInternalParams.


        :param source_name: The source_name of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def destination_name(self):
        """Gets the destination_name of this BTTranslateInternalParams.  # noqa: E501


        :return: The destination_name of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this BTTranslateInternalParams.


        :param destination_name: The destination_name of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._destination_name = destination_name

    @property
    def text_as_geometry(self):
        """Gets the text_as_geometry of this BTTranslateInternalParams.  # noqa: E501


        :return: The text_as_geometry of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._text_as_geometry

    @text_as_geometry.setter
    def text_as_geometry(self, text_as_geometry):
        """Sets the text_as_geometry of this BTTranslateInternalParams.


        :param text_as_geometry: The text_as_geometry of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._text_as_geometry = text_as_geometry

    @property
    def flatten(self):
        """Gets the flatten of this BTTranslateInternalParams.  # noqa: E501


        :return: The flatten of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._flatten

    @flatten.setter
    def flatten(self, flatten):
        """Sets the flatten of this BTTranslateInternalParams.


        :param flatten: The flatten of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._flatten = flatten

    @property
    def include_export_ids(self):
        """Gets the include_export_ids of this BTTranslateInternalParams.  # noqa: E501


        :return: The include_export_ids of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_export_ids

    @include_export_ids.setter
    def include_export_ids(self, include_export_ids):
        """Sets the include_export_ids of this BTTranslateInternalParams.


        :param include_export_ids: The include_export_ids of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._include_export_ids = include_export_ids

    @property
    def show_overridden_dimensions(self):
        """Gets the show_overridden_dimensions of this BTTranslateInternalParams.  # noqa: E501


        :return: The show_overridden_dimensions of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_overridden_dimensions

    @show_overridden_dimensions.setter
    def show_overridden_dimensions(self, show_overridden_dimensions):
        """Sets the show_overridden_dimensions of this BTTranslateInternalParams.


        :param show_overridden_dimensions: The show_overridden_dimensions of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._show_overridden_dimensions = show_overridden_dimensions

    @property
    def current_sheet_only(self):
        """Gets the current_sheet_only of this BTTranslateInternalParams.  # noqa: E501


        :return: The current_sheet_only of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._current_sheet_only

    @current_sheet_only.setter
    def current_sheet_only(self, current_sheet_only):
        """Sets the current_sheet_only of this BTTranslateInternalParams.


        :param current_sheet_only: The current_sheet_only of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._current_sheet_only = current_sheet_only

    @property
    def image_width(self):
        """Gets the image_width of this BTTranslateInternalParams.  # noqa: E501


        :return: The image_width of this BTTranslateInternalParams.  # noqa: E501
        :rtype: int
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this BTTranslateInternalParams.


        :param image_width: The image_width of this BTTranslateInternalParams.  # noqa: E501
        :type: int
        """

        self._image_width = image_width

    @property
    def image_height(self):
        """Gets the image_height of this BTTranslateInternalParams.  # noqa: E501


        :return: The image_height of this BTTranslateInternalParams.  # noqa: E501
        :rtype: int
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this BTTranslateInternalParams.


        :param image_height: The image_height of this BTTranslateInternalParams.  # noqa: E501
        :type: int
        """

        self._image_height = image_height

    @property
    def color_method(self):
        """Gets the color_method of this BTTranslateInternalParams.  # noqa: E501


        :return: The color_method of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._color_method

    @color_method.setter
    def color_method(self, color_method):
        """Sets the color_method of this BTTranslateInternalParams.


        :param color_method: The color_method of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._color_method = color_method

    @property
    def splines_as_polylines(self):
        """Gets the splines_as_polylines of this BTTranslateInternalParams.  # noqa: E501


        :return: The splines_as_polylines of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._splines_as_polylines

    @splines_as_polylines.setter
    def splines_as_polylines(self, splines_as_polylines):
        """Sets the splines_as_polylines of this BTTranslateInternalParams.


        :param splines_as_polylines: The splines_as_polylines of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._splines_as_polylines = splines_as_polylines

    @property
    def selectable_pdf_text(self):
        """Gets the selectable_pdf_text of this BTTranslateInternalParams.  # noqa: E501


        :return: The selectable_pdf_text of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._selectable_pdf_text

    @selectable_pdf_text.setter
    def selectable_pdf_text(self, selectable_pdf_text):
        """Sets the selectable_pdf_text of this BTTranslateInternalParams.


        :param selectable_pdf_text: The selectable_pdf_text of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._selectable_pdf_text = selectable_pdf_text

    @property
    def grouping(self):
        """Gets the grouping of this BTTranslateInternalParams.  # noqa: E501


        :return: The grouping of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._grouping

    @grouping.setter
    def grouping(self, grouping):
        """Sets the grouping of this BTTranslateInternalParams.


        :param grouping: The grouping of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._grouping = grouping

    @property
    def import_in_background(self):
        """Gets the import_in_background of this BTTranslateInternalParams.  # noqa: E501


        :return: The import_in_background of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._import_in_background

    @import_in_background.setter
    def import_in_background(self, import_in_background):
        """Sets the import_in_background of this BTTranslateInternalParams.


        :param import_in_background: The import_in_background of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._import_in_background = import_in_background

    @property
    def project_id(self):
        """Gets the project_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The project_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTTranslateInternalParams.


        :param project_id: The project_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def parent_id(self):
        """Gets the parent_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The parent_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BTTranslateInternalParams.


        :param parent_id: The parent_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def foreign_id(self):
        """Gets the foreign_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The foreign_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, foreign_id):
        """Sets the foreign_id of this BTTranslateInternalParams.


        :param foreign_id: The foreign_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._foreign_id = foreign_id

    @property
    def upload_id(self):
        """Gets the upload_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The upload_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this BTTranslateInternalParams.


        :param upload_id: The upload_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._upload_id = upload_id

    @property
    def specify_units(self):
        """Gets the specify_units of this BTTranslateInternalParams.  # noqa: E501


        :return: The specify_units of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._specify_units

    @specify_units.setter
    def specify_units(self, specify_units):
        """Sets the specify_units of this BTTranslateInternalParams.


        :param specify_units: The specify_units of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._specify_units = specify_units

    @property
    def unit(self):
        """Gets the unit of this BTTranslateInternalParams.  # noqa: E501


        :return: The unit of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this BTTranslateInternalParams.


        :param unit: The unit of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def original_foreign_id(self):
        """Gets the original_foreign_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The original_foreign_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._original_foreign_id

    @original_foreign_id.setter
    def original_foreign_id(self, original_foreign_id):
        """Sets the original_foreign_id of this BTTranslateInternalParams.


        :param original_foreign_id: The original_foreign_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._original_foreign_id = original_foreign_id

    @property
    def import_within_document(self):
        """Gets the import_within_document of this BTTranslateInternalParams.  # noqa: E501


        :return: The import_within_document of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._import_within_document

    @import_within_document.setter
    def import_within_document(self, import_within_document):
        """Sets the import_within_document of this BTTranslateInternalParams.


        :param import_within_document: The import_within_document of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._import_within_document = import_within_document

    @property
    def blob_element_id(self):
        """Gets the blob_element_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The blob_element_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_element_id

    @blob_element_id.setter
    def blob_element_id(self, blob_element_id):
        """Sets the blob_element_id of this BTTranslateInternalParams.


        :param blob_element_id: The blob_element_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._blob_element_id = blob_element_id

    @property
    def blob_microversion_id(self):
        """Gets the blob_microversion_id of this BTTranslateInternalParams.  # noqa: E501


        :return: The blob_microversion_id of this BTTranslateInternalParams.  # noqa: E501
        :rtype: str
        """
        return self._blob_microversion_id

    @blob_microversion_id.setter
    def blob_microversion_id(self, blob_microversion_id):
        """Sets the blob_microversion_id of this BTTranslateInternalParams.


        :param blob_microversion_id: The blob_microversion_id of this BTTranslateInternalParams.  # noqa: E501
        :type: str
        """

        self._blob_microversion_id = blob_microversion_id

    @property
    def split_assemblies_into_multiple_documents(self):
        """Gets the split_assemblies_into_multiple_documents of this BTTranslateInternalParams.  # noqa: E501


        :return: The split_assemblies_into_multiple_documents of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._split_assemblies_into_multiple_documents

    @split_assemblies_into_multiple_documents.setter
    def split_assemblies_into_multiple_documents(self, split_assemblies_into_multiple_documents):
        """Sets the split_assemblies_into_multiple_documents of this BTTranslateInternalParams.


        :param split_assemblies_into_multiple_documents: The split_assemblies_into_multiple_documents of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._split_assemblies_into_multiple_documents = split_assemblies_into_multiple_documents

    @property
    def flatten_assemblies(self):
        """Gets the flatten_assemblies of this BTTranslateInternalParams.  # noqa: E501


        :return: The flatten_assemblies of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._flatten_assemblies

    @flatten_assemblies.setter
    def flatten_assemblies(self, flatten_assemblies):
        """Sets the flatten_assemblies of this BTTranslateInternalParams.


        :param flatten_assemblies: The flatten_assemblies of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._flatten_assemblies = flatten_assemblies

    @property
    def gety_axis_is_up(self):
        """Gets the gety_axis_is_up of this BTTranslateInternalParams.  # noqa: E501


        :return: The gety_axis_is_up of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._gety_axis_is_up

    @gety_axis_is_up.setter
    def gety_axis_is_up(self, gety_axis_is_up):
        """Sets the gety_axis_is_up of this BTTranslateInternalParams.


        :param gety_axis_is_up: The gety_axis_is_up of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._gety_axis_is_up = gety_axis_is_up

    @property
    def allow_faulty_parts(self):
        """Gets the allow_faulty_parts of this BTTranslateInternalParams.  # noqa: E501


        :return: The allow_faulty_parts of this BTTranslateInternalParams.  # noqa: E501
        :rtype: bool
        """
        return self._allow_faulty_parts

    @allow_faulty_parts.setter
    def allow_faulty_parts(self, allow_faulty_parts):
        """Sets the allow_faulty_parts of this BTTranslateInternalParams.


        :param allow_faulty_parts: The allow_faulty_parts of this BTTranslateInternalParams.  # noqa: E501
        :type: bool
        """

        self._allow_faulty_parts = allow_faulty_parts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTTranslateInternalParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
