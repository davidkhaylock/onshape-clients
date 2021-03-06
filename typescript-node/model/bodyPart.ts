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

import { BodyPartHeaders } from './bodyPartHeaders';
import { BodyPartMediaType } from './bodyPartMediaType';
import { ContentDisposition } from './contentDisposition';
import { MessageBodyWorkers } from './messageBodyWorkers';
import { MultiPart } from './multiPart';

export class BodyPart {
    'contentDisposition'?: ContentDisposition;
    'entity'?: any;
    'headers'?: BodyPartHeaders;
    'mediaType'?: BodyPartMediaType;
    'messageBodyWorkers'?: MessageBodyWorkers;
    'parent'?: MultiPart;
    'providers'?: any;
    'parameterizedHeaders'?: BodyPartHeaders;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "contentDisposition",
            "baseName": "contentDisposition",
            "type": "ContentDisposition"
        },
        {
            "name": "entity",
            "baseName": "entity",
            "type": "any"
        },
        {
            "name": "headers",
            "baseName": "headers",
            "type": "BodyPartHeaders"
        },
        {
            "name": "mediaType",
            "baseName": "mediaType",
            "type": "BodyPartMediaType"
        },
        {
            "name": "messageBodyWorkers",
            "baseName": "messageBodyWorkers",
            "type": "MessageBodyWorkers"
        },
        {
            "name": "parent",
            "baseName": "parent",
            "type": "MultiPart"
        },
        {
            "name": "providers",
            "baseName": "providers",
            "type": "any"
        },
        {
            "name": "parameterizedHeaders",
            "baseName": "parameterizedHeaders",
            "type": "BodyPartHeaders"
        }    ];

    static getAttributeTypeMap() {
        return BodyPart.attributeTypeMap;
    }
}

