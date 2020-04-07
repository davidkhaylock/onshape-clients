/*
 * Onshape REST API
 *
 * The Onshape REST API consumed by all clients.
 *
 * API version: 1.111
 * Contact: api-support@onshape.zendesk.com
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// BtExportModelLoop1182 struct for BtExportModelLoop1182
type BtExportModelLoop1182 struct {
	Coedges []BtExportModelCoedge1342 `json:"coedges,omitempty"`
	IsInner bool `json:"isInner,omitempty"`
	IsOuter bool `json:"isOuter,omitempty"`
}