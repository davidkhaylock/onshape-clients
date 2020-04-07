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
// BtWebhookParams struct for BtWebhookParams
type BtWebhookParams struct {
	ClientId string `json:"clientId,omitempty"`
	CompanyId string `json:"companyId,omitempty"`
	Data string `json:"data,omitempty"`
	DocumentId string `json:"documentId,omitempty"`
	ElementId string `json:"elementId,omitempty"`
	Events []string `json:"events,omitempty"`
	Filter string `json:"filter,omitempty"`
	FolderId string `json:"folderId,omitempty"`
	Id string `json:"id,omitempty"`
	Options BtWebhookOptions `json:"options,omitempty"`
	PartId string `json:"partId,omitempty"`
	ProjectId string `json:"projectId,omitempty"`
	Url string `json:"url,omitempty"`
	UserId string `json:"userId,omitempty"`
	VersionId string `json:"versionId,omitempty"`
	WorkspaceId string `json:"workspaceId,omitempty"`
}