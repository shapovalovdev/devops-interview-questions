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
{{- if .Values.image.local }}
{{- if .Values.image.digest }}
{{- printf "%s@%s" $repository .Values.image.digest }}
{{- else }}
{{- $tag := required "image.tag is required when image.local is true and image.digest is unset" .Values.image.tag }}
{{- printf "%s:%s" $repository $tag }}
{{- end }}
{{- else }}
{{- $digest := required "image.digest is required when image.local is false" .Values.image.digest }}
{{- if not (regexMatch "^sha256:[a-f0-9]{64}$" $digest) }}{{ fail "image.digest must be a sha256 digest when image.local is false" }}{{ end }}
{{- printf "%s@%s" $repository $digest }}
{{- end }}
{{- end }}
