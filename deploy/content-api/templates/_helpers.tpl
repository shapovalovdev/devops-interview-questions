{{- define "content-api.name" -}}
content-api
{{- end }}

{{- define "content-api.fullname" -}}
{{- .Release.Name }}
{{- end }}

{{- define "content-api.labels" -}}
app.kubernetes.io/name: {{ include "content-api.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: Helm
{{- end }}

{{- define "content-api.image" -}}
{{- $repository := required "image.repository is required" .Values.image.repository }}
{{- if .Values.image.digest }}
{{- printf "%s@%s" $repository .Values.image.digest }}
{{- else }}
{{- $tag := required "image.tag is required when image.digest is unset" .Values.image.tag }}
{{- if and (not .Values.image.local) (eq $tag "latest") }}{{ fail "image.tag must not be latest outside the local k3d overlay" }}{{ end }}
{{- printf "%s:%s" $repository $tag }}
{{- end }}
{{- end }}
