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

import { BTConnection } from './bTConnection';

export class BTOccurrence {
    'fullPathAsString'?: string;
    'rootOccurrence'?: boolean;
    'tailInstanceId'?: string;
    'headInstanceId'?: string;
    'occurrenceWithoutHead'?: BTOccurrence;
    'occurrenceWithoutTail'?: BTOccurrence;
    'path'?: Array<string>;
    'typeId'?: number;
    'exportTypeName'?: string;
    'connectionSource'?: BTConnection;
    'unknownClass'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "fullPathAsString",
            "baseName": "fullPathAsString",
            "type": "string"
        },
        {
            "name": "rootOccurrence",
            "baseName": "rootOccurrence",
            "type": "boolean"
        },
        {
            "name": "tailInstanceId",
            "baseName": "tailInstanceId",
            "type": "string"
        },
        {
            "name": "headInstanceId",
            "baseName": "headInstanceId",
            "type": "string"
        },
        {
            "name": "occurrenceWithoutHead",
            "baseName": "occurrenceWithoutHead",
            "type": "BTOccurrence"
        },
        {
            "name": "occurrenceWithoutTail",
            "baseName": "occurrenceWithoutTail",
            "type": "BTOccurrence"
        },
        {
            "name": "path",
            "baseName": "path",
            "type": "Array<string>"
        },
        {
            "name": "typeId",
            "baseName": "typeId",
            "type": "number"
        },
        {
            "name": "exportTypeName",
            "baseName": "exportTypeName",
            "type": "string"
        },
        {
            "name": "connectionSource",
            "baseName": "connectionSource",
            "type": "BTConnection"
        },
        {
            "name": "unknownClass",
            "baseName": "unknownClass",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTOccurrence.attributeTypeMap;
    }
}

