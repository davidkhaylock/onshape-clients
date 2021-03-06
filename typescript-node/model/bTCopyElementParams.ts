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


export class BTCopyElementParams {
    'documentIdSource'?: string;
    'workspaceIdSource'?: string;
    'elementIdSource'?: string;
    'anchorElementId'?: string;
    'isGroupAnchor'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "documentIdSource",
            "baseName": "documentIdSource",
            "type": "string"
        },
        {
            "name": "workspaceIdSource",
            "baseName": "workspaceIdSource",
            "type": "string"
        },
        {
            "name": "elementIdSource",
            "baseName": "elementIdSource",
            "type": "string"
        },
        {
            "name": "anchorElementId",
            "baseName": "anchorElementId",
            "type": "string"
        },
        {
            "name": "isGroupAnchor",
            "baseName": "isGroupAnchor",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTCopyElementParams.attributeTypeMap;
    }
}

