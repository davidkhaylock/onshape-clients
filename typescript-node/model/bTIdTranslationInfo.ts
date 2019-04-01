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

import { BTIdTranslationResultInfo } from './bTIdTranslationResultInfo';

export class BTIdTranslationInfo {
    'sourceDocumentMicroversion'?: string;
    'targetDocumentMicroversion'?: string;
    'ids'?: Array<BTIdTranslationResultInfo>;
    'documentId'?: string;
    'elementId'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "sourceDocumentMicroversion",
            "baseName": "sourceDocumentMicroversion",
            "type": "string"
        },
        {
            "name": "targetDocumentMicroversion",
            "baseName": "targetDocumentMicroversion",
            "type": "string"
        },
        {
            "name": "ids",
            "baseName": "ids",
            "type": "Array<BTIdTranslationResultInfo>"
        },
        {
            "name": "documentId",
            "baseName": "documentId",
            "type": "string"
        },
        {
            "name": "elementId",
            "baseName": "elementId",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTIdTranslationInfo.attributeTypeMap;
    }
}
