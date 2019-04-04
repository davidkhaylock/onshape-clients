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

import { BTExternalElementReferenceInfo } from './bTExternalElementReferenceInfo';
import { BTPartMaterialPropertyInfo } from './bTPartMaterialPropertyInfo';

export class BTPartMaterialInfo {
    'properties'?: Array<BTPartMaterialPropertyInfo>;
    'id'?: string;
    'displayName'?: string;
    'libraryName'?: string;
    'libraryReference'?: BTExternalElementReferenceInfo;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "properties",
            "baseName": "properties",
            "type": "Array<BTPartMaterialPropertyInfo>"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "displayName",
            "baseName": "displayName",
            "type": "string"
        },
        {
            "name": "libraryName",
            "baseName": "libraryName",
            "type": "string"
        },
        {
            "name": "libraryReference",
            "baseName": "libraryReference",
            "type": "BTExternalElementReferenceInfo"
        }    ];

    static getAttributeTypeMap() {
        return BTPartMaterialInfo.attributeTypeMap;
    }
}
