{{/* vim: set filetype=mustache: */}}

{{- define "color-grid.name" -}}
{{ default "color-grid" .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "color-grid.fullname" -}}
{{ if .Values.fullnameOverride }}
{{ .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "color-grid" | trunc 63 | trimSuffix "-" }}
{{- end -}}
{{- end -}}

{{- define "color-grid.labels" -}}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
app.kubernetes.io/name: {{ include "color-grid.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
