/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { BTMetadataPropertyConfigParams } from './bTMetadataPropertyConfigParams';

export class BTMetadataPropertyParams {
    'array'?: boolean;
    'name'?: string;
    'id'?: string;
    'description'?: string;
    'namespace'?: string;
    'ownerId'?: string;
    'propertyConfigParamList'?: Array<BTMetadataPropertyConfigParams>;
    'valueType'?: number;
    'ownerTypeOrdinal'?: number;
    'objectDefName'?: string;
    'blobMimeType'?: string;
    'editableInVersion'?: boolean;
    'editableInMicroversion'?: boolean;
    'searchBoost'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "array",
            "baseName": "array",
            "type": "boolean"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "namespace",
            "baseName": "namespace",
            "type": "string"
        },
        {
            "name": "ownerId",
            "baseName": "ownerId",
            "type": "string"
        },
        {
            "name": "propertyConfigParamList",
            "baseName": "propertyConfigParamList",
            "type": "Array<BTMetadataPropertyConfigParams>"
        },
        {
            "name": "valueType",
            "baseName": "valueType",
            "type": "number"
        },
        {
            "name": "ownerTypeOrdinal",
            "baseName": "ownerTypeOrdinal",
            "type": "number"
        },
        {
            "name": "objectDefName",
            "baseName": "objectDefName",
            "type": "string"
        },
        {
            "name": "blobMimeType",
            "baseName": "blobMimeType",
            "type": "string"
        },
        {
            "name": "editableInVersion",
            "baseName": "editableInVersion",
            "type": "boolean"
        },
        {
            "name": "editableInMicroversion",
            "baseName": "editableInMicroversion",
            "type": "boolean"
        },
        {
            "name": "searchBoost",
            "baseName": "searchBoost",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return BTMetadataPropertyParams.attributeTypeMap;
    }
}

