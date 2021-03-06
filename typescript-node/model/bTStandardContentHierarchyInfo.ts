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

import { VersionSpecs } from './versionSpecs';

export class BTStandardContentHierarchyInfo {
    'type'?: string;
    'existingVersions'?: Array<VersionSpecs>;
    'category'?: string;
    'standard'?: string;
    'types'?: string;
    'productionVersionId'?: string;
    'testVersionId'?: string;
    'documentType'?: number;
    'defaultWorkspace'?: string;
    'name'?: string;
    'id'?: string;
    'href'?: string;
    'viewRef'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "type",
            "type": "string"
        },
        {
            "name": "existingVersions",
            "baseName": "existingVersions",
            "type": "Array<VersionSpecs>"
        },
        {
            "name": "category",
            "baseName": "category",
            "type": "string"
        },
        {
            "name": "standard",
            "baseName": "standard",
            "type": "string"
        },
        {
            "name": "types",
            "baseName": "types",
            "type": "string"
        },
        {
            "name": "productionVersionId",
            "baseName": "productionVersionId",
            "type": "string"
        },
        {
            "name": "testVersionId",
            "baseName": "testVersionId",
            "type": "string"
        },
        {
            "name": "documentType",
            "baseName": "documentType",
            "type": "number"
        },
        {
            "name": "defaultWorkspace",
            "baseName": "defaultWorkspace",
            "type": "string"
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
            "name": "href",
            "baseName": "href",
            "type": "string"
        },
        {
            "name": "viewRef",
            "baseName": "viewRef",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return BTStandardContentHierarchyInfo.attributeTypeMap;
    }
}

