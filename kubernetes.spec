        
%if 0%{?fedora}
%global with_devel 1
%global with_bundled 1
%global with_debug 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%endif

%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global provider	    github
%global provider_tld	com
%global project		    GoogleCloudPlatform
%global repo		    kubernetes
# https://github.com/GoogleCloudPlatform/kubernetes
%global import_path	    %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit		    6a5c06e3d1eb27a6310a09270e4a5fb1afa93e74
%global shortcommit	    %(c=%{commit}; echo ${c:0:7})

#I really need this, otherwise "version_ldflags=$(kube::version_ldflags)"
# does not work
%global _buildshell	/bin/bash
%global _checkshell	/bin/bash

Name:		kubernetes
Version:	1.1.3
Release:	4%{?dist}.cloudlinux
Epoch:      1
Summary:    Container cluster management
License:    ASL 2.0
URL:        %{import_path}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: x86_64

Source0: %{name}-%{version}.tar.gz
Source1: genmanpages.sh
Source2: kube-apiserver.service
Source3: kube-controller-manager.service
Source4: kube-scheduler.service
Source5: kubelet.service
Source6: kube-proxy.service
Source7: kube-proxy.init
Source8: kubernetes.conf
Source9: apiserver
Source10: config
Source11: controller-manager
Source12: kubelet
Source13: proxy
Source14: scheduler

# Patch0: kuberdock-1.1.3.patch

Requires: %{name}-master = %{epoch}:%{version}-%{release}
Requires: %{name}-node = %{epoch}:%{version}-%{release}

%description
%{summary}

%if 0%{?rhel} >= 7
%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildRequires: golang >= 1.2.1-3

Provides: golang(%{import_path}/cmd/genutils) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kube-apiserver/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kube-controller-manager/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kube-proxy/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kubelet/app) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/archive) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/assert) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/backoff) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/controllermanager) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/election) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/executor) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/executor/config) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/executor/messages) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/executor/service) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/hyperkube) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/offers) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/offers/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/proc) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/profile) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/queue) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/redirfd) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/runtime) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/config) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/constraint) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/ha) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/meta) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/podtask) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/service) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/scheduler/uid) = %{version}-%{release}
Provides: golang(%{import_path}/contrib/mesos/pkg/service) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/admission) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/endpoints) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/errors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/errors/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/meta) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/registered) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/resource) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/rest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/rest/resttest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/testapi) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/testing) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/v1) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/v1beta3) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/validation) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/apiserver) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/apiserver/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authenticator) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authenticator/bearertoken) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authorizer) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authorizer/abac) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/handlers) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/user) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/capabilities) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/cache) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/chaosclient) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api/v1) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/portforward) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/record) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/remotecommand) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/testclient) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/clientauth) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/aws) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/fake) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/gce) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/mesos) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/nodecontroller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/openstack) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/ovirt) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/rackspace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/routecontroller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/servicecontroller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/vagrant) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/controller/framework) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/conversion) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/conversion/queryparams) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/credentialprovider) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/credentialprovider/gcp) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/fieldpath) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/fields) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/healthz) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/httplog) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/hyperkube) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/resource) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/cadvisor) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/container) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/dockertools) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/envvars) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/leaky) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/lifecycle) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/network) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/network/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/prober) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/rkt) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/types) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/labels) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/master) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/master/ports) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/namespace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/http) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/tcp) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/proxy) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/proxy/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/componentstatus) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/controller/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/endpoint) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/endpoint/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/event) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic/rest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/limitrange) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/minion) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/minion/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/namespace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/namespace/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolume) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolume/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolumeclaim) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolumeclaim/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/pod) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/pod/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/podtemplate) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/podtemplate/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/registrytest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/resourcequota/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/secret) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/secret/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/allocator) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/allocator/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/ipallocator) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/ipallocator/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/ipallocator/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/portallocator) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service/portallocator/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/serviceaccount) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/serviceaccount/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/runtime) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/securitycontext) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/service) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/serviceaccount) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/tools) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/tools/etcdtest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/types) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ui) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ui/data/dashboard) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ui/data/swagger) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/errors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/fielderrors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/flushwriter) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/httpstream) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/httpstream/spdy) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/iptables) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/mount) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/node) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/operationmanager) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/proxy) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/slice) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/strategicpatch) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/wait) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/workqueue) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/yaml) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/version) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/version/verflag) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/aws_ebs) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/empty_dir) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/gce_pd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/git_repo) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/glusterfs) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/host_path) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/iscsi) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/nfs) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/persistent_claim) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/rbd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/secret) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volumeclaimbinder) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/watch) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/watch/json) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/cmd/kube-scheduler/app) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/admit) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/deny) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/exec/denyprivileged) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/limitranger) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/autoprovision) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/exists) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/lifecycle) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/securitycontext/scdeny) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/serviceaccount) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/password) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/password/allow) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/password/passwordfile) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/basicauth) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/union) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/x509) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/token/tokenfile) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/token/tokentest) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithm) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithm/predicates) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithm/priorities) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithmprovider) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithmprovider/defaults) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/v1) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/validation) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/factory) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/test/e2e) = %{version}-%{release}
Provides: golang(%{import_path}/test/integration) = %{version}-%{release}
Provides: golang(%{import_path}/test/integration/framework) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for
building other packages which use %{project}/%{repo}.
%endif

%package unit-test
Epoch: 1
Summary: %{summary} - for running unit tests

# below Rs used for testing
Requires: golang >= 1.2-7
Requires: etcd >= 2.0.9
Requires: hostname
Requires: rsync
Requires: NetworkManager

%description unit-test
%{summary} - for running unit tests

%package master
Epoch: 1
Summary: Kubernetes services for master host

BuildRequires: golang >= 1.2-7
BuildRequires: systemd
BuildRequires: rsync
BuildRequires: go-md2man

Requires(pre): shadow-utils
Requires: %{name}-client = %{epoch}:%{version}-%{release}

Conflicts: %{name}-node < %{epoch}:%{version}-%{release}
Conflicts: %{name}-node > %{epoch}:%{version}-%{release}

%description master
Kubernetes services for master host

%package node
Epoch: 1
Summary: Kubernetes services for node host

BuildRequires: golang >= 1.2-7
BuildRequires: systemd
BuildRequires: rsync
BuildRequires: go-md2man

Requires(pre): shadow-utils
Requires: socat
Requires: %{name}-client = %{epoch}:%{version}-%{release}

Conflicts: %{name}-master < %{epoch}:%{version}-%{release}
Conflicts: %{name}-master > %{epoch}:%{version}-%{release}

%description node
Kubernetes services for node host

%package client
Epoch: 1
Summary: Kubernetes client tools

BuildRequires: golang >= 1.2-7

%description client
Kubernetes client tools like kubectl
%endif

%package proxy
Epoch: 1
Summary: Kubernetes services for node host

BuildRequires: golang >= 1.2-7
BuildRequires: rsync
BuildRequires: go-md2man

Requires(pre): shadow-utils

Conflicts: %{name}-master < %{epoch}:%{version}-%{release}
Conflicts: %{name}-master > %{epoch}:%{version}-%{release}

%description proxy
Kubernetes services for node host


%prep
%setup -qn %{name}-%{version}
# %patch0 -p1


%build
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_COMMIT=%{commit}
export KUBE_GIT_VERSION=v1.0.0-290-gb2dafdaef5acea

hack/build-go.sh --use_go_build
hack/build-go.sh --use_go_build cmd/kube-version-change

# convert md to man
pushd docs
pushd admin
cp kube-apiserver.md kube-controller-manager.md kube-proxy.md kube-scheduler.md kubelet.md ..
popd
cp %{SOURCE1} genmanpages.sh
bash genmanpages.sh
popd


%install
. hack/lib/init.sh
kube::golang::setup_env

output_path="${KUBE_OUTPUT_BINPATH}/$(kube::golang::current_platform)"

binaries=(kube-apiserver kube-controller-manager kube-scheduler kube-proxy kubelet kubectl kube-version-change)
install -m 755 -d %{buildroot}%{_bindir}
for bin in "${binaries[@]}"; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/${bin}
done

# install the bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
install -t %{buildroot}%{_datadir}/bash-completion/completions/ contrib/completions/bash/kubectl

# install config files
#install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
#install -m 644 -t %{buildroot}%{_sysconfdir}/%{name} contrib/init/systemd/environ/*

# install service files
%if 0%{?rhel} >= 7
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE2}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE3}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE4}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE5}
install -m 0644 -t %{buildroot}%{_unitdir} %{SOURCE6}
%else
install -D -p -m 755 %{SOURCE7} %{buildroot}%{_sysconfdir}/rc.d/init.d/kube-proxy
%endif

# install config files
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE9}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE10}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE11}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE12}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE13}
install -m 0644 -t %{buildroot}%{_sysconfdir}/%{name} %{SOURCE14}

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/* %{buildroot}%{_mandir}/man1

# install the place the kubelet defaults to put volumes
install -d %{buildroot}%{_sharedstatedir}/kubelet

# place contrib/init/systemd/tmpfiles.d/kubernetes.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -p -m 0644 -t %{buildroot}%{_tmpfilesdir} %{SOURCE8}

%if 0%{?with_debug}
# remove porter as it is built inside docker container without options for debug info
rm -rf contrib/for-tests/porter
%endif

%if 0%{?with_devel}
# install devel source codes
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in build cluster cmd contrib examples hack pkg plugin test; do
    cp -rpav $d %{buildroot}/%{gopath}/src/%{import_path}/
done
%endif

# place files for unit-test rpm
install -d -m 0755 %{buildroot}%{_sharedstatedir}/kubernetes-unit-test/
cp -pav README.md %{buildroot}%{_sharedstatedir}/kubernetes-unit-test/.
for d in _output Godeps api cmd docs examples hack pkg plugin third_party test; do
  cp -a $d %{buildroot}%{_sharedstatedir}/kubernetes-unit-test/
done


%check
# Fedora, RHEL7 and CentOS are tested via unit-test subpackage
if [ 1 != 1 ]; then
echo "******Testing the commands*****"
hack/test-cmd.sh
echo "******Benchmarking kube********"
hack/benchmark-go.sh

# In Fedora 20 and RHEL7 the go cover tools isn't available correctly
%if 0%{?fedora} >= 21
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing integration******"
hack/test-integration.sh --use_go_build
%endif
fi


%if 0%{?rhel} >= 7
%pre master
getent group kube >/dev/null || groupadd -r kube
getent passwd kube >/dev/null || useradd -r -g kube -d / -s /sbin/nologin \
        -c "Kubernetes user" kube

%post master
%systemd_post kube-apiserver kube-scheduler kube-controller-manager

%preun master
%systemd_preun kube-apiserver kube-scheduler kube-controller-manager

%postun master
%systemd_postun


%pre node
getent group kube >/dev/null || groupadd -r kube
getent passwd kube >/dev/null || useradd -r -g kube -d / -s /sbin/nologin \
        -c "Kubernetes user" kube

%post node
%systemd_post kubelet kube-proxy

%preun node
%systemd_preun kubelet kube-proxy

%postun node
%systemd_postun


%files
# empty as it depends on master and node

%files master
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%{_mandir}/man1/kube-apiserver.1*
%{_mandir}/man1/kube-controller-manager.1*
%{_mandir}/man1/kube-scheduler.1*
%{_mandir}/man1/kubectl.1*
%{_mandir}/man1/kubectl-*
%caps(cap_net_bind_service=ep) %{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_bindir}/kube-version-change
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-scheduler.service
%config(noreplace) %{_sysconfdir}/%{name}/apiserver
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/controller-manager
%config(noreplace) %{_sysconfdir}/%{name}/scheduler
%{_tmpfilesdir}/kubernetes.conf

%files node
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%{_mandir}/man1/kubelet.1*
%{_mandir}/man1/kube-proxy.1*
%{_bindir}/kubelet
%{_bindir}/kube-proxy
%{_bindir}/kube-version-change
%{_bindir}/kubectl
%{_unitdir}/kubelet.service
%{_unitdir}/kube-proxy.service
%dir %attr(0755,kube,kube) %{_sharedstatedir}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%{_tmpfilesdir}/kubernetes.conf

%files client
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%{_mandir}/man1/kubectl.1*
%{_mandir}/man1/kubectl-*
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl

%files unit-test
%{_sharedstatedir}/kubernetes-unit-test/

%if 0%{?with_devel}
%files devel
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}
%endif
%endif

%files proxy
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%{_mandir}/man1/kube-proxy.1*
%{_bindir}/kube-proxy
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%if 0%{?rhel} >= 7
%{_unitdir}/kube-proxy.service
%else
%{_sysconfdir}/rc.d/init.d/kube-proxy
%exclude %{_mandir}/man1/kube-apiserver.1*
%exclude %{_mandir}/man1/kube-controller-manager.1*
%exclude %{_mandir}/man1/kube-scheduler.1*
%exclude %{_mandir}/man1/kubectl.1*
%exclude %{_mandir}/man1/kubectl-*
%exclude %{_mandir}/man1/kubelet.1*
%exclude %{_mandir}/man1/kubectl.1*
%exclude %{_mandir}/man1/kubectl-*
%exclude %{_bindir}/kube-apiserver
%exclude %{_bindir}/kube-controller-manager
%exclude %{_bindir}/kube-scheduler
%exclude %{_bindir}/kube-version-change
%exclude %{_bindir}/kubectl
%exclude %{_bindir}/kubelet
%exclude %{_bindir}/kube-version-change
%exclude %{_bindir}/kubectl
%exclude %{_bindir}/kubectl
%exclude %{_datadir}/bash-completion/completions/kubectl
%exclude %{_datadir}/bash-completion/completions/kubectl
%exclude %{_sharedstatedir}/kubernetes-unit-test/
%exclude %{_sysconfdir}/%{name}/apiserver
%exclude %{_sysconfdir}/%{name}/controller-manager
%exclude %{_sysconfdir}/%{name}/scheduler
%exclude %{_sysconfdir}/%{name}/kubelet
%endif


%changelog
* Wed Feb 24 2016 Sergey Fokin <sfokin@cloudlinux.com> - 1.1.3-3.cloudlinux
- some changes in kuberdock-1.1.3.patch

* Fri Jan 22 2016 Sergey Fokin <sfokin@cloudlinux.com> - 1.1.3-2.cloudlinux
- add %{_prefix}/lib/kubernetes.conf

* Tue Jan 19 2016 Sergey Fokin <sfokin@cloudlinux.com> - 1.1.3-1.cloudlinux
- update to 1.1.3
- add kuberdock-1.1.3.patch

* Mon Nov 16 2015 Sergey Fokin <sfokin@cloudlinux.com> - 1.1.1-1
- update to 1.1.1

* Fri Jul 17 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.6.gitb2dafda
- Bump to upstream b2dafdaef5aceafad503ab56254b60f80da9e980
  related: #1211266

* Thu Jul 16 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.5.git596a8a4
- Bump to upstream 596a8a40d12498b5335140f50753980bfaea4f6b
  related: #1211266

* Wed Jul 15 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.4.git6ba532b
- Bump to upstream 6ba532b218cb5f5ea3f0e8dce5395182f388536c
  related: #1211266

* Tue Jul 14 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.3.gitc616182
- Bump to upstream c6161824db3784e6156131307a5e94647e5557fd
  related: #1211266

* Mon Jul 13 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.2.git2c27b1f
- Bump to upstream 2c27b1fa64f4e70f04575d1b217494f49332390e
  related: #1211266

* Sat Jul 11 2015 jchaloup <jchaloup@redhat.com> - 1.0.0-0.1.git1b37059
- Bump to upstream 1b370599ccf271741e657335c4943cb8c7dba28b
  related: #1211266

* Fri Jul 10 2015 jchaloup <jchaloup@redhat.com> - 0.21.1-0.2.gitccc4cfc
- Bump to upstream ccc4cfc7e11e0f127ac1cea045017dd799be3c63
  related: #1211266

* Thu Jul 09 2015 jchaloup <jchaloup@redhat.com> - 0.21.1-0.1.git41f8907
- Update generating of man pages from md (add genmanpages.sh)
- Bump to upstream 41f89075396329cd46c58495c7d3f7e13adcaa96
  related: #1211266

* Wed Jul 08 2015 jchaloup <jchaloup@redhat.com> - 0.20.2-0.5.git77be29e
- Bump to upstream 77be29e3da71f0a136b6aa4048b2f0575c2598e4
  related: #1211266

* Tue Jul 07 2015 jchaloup <jchaloup@redhat.com> - 0.20.2-0.4.git639a7da
- Bump to upstream 639a7dac50a331414cc6c47083323388da0d8756
  related: #1211266

* Mon Jul 06 2015 jchaloup <jchaloup@redhat.com> - 0.20.2-0.3.gitbb6f2f7
- Bump to upstream bb6f2f7ad90596d624d84cc691eec0f518e90cc8
  related: #1211266

* Fri Jul 03 2015 jchaloup <jchaloup@redhat.com> - 0.20.2-0.2.git974377b
- Bump to upstream 974377b3064ac59b6e5694bfa568d67128026171
  related: #1211266

* Thu Jul 02 2015 jchaloup <jchaloup@redhat.com> - 0.20.2-0.1.gitef41ceb
- Bump to upstream ef41ceb3e477ceada84c5522f429f02ab0f5948e
  related: #1211266

* Tue Jun 30 2015 jchaloup <jchaloup@redhat.com> - 0.20.0-0.3.git835eded
- Bump to upstream 835eded2943dfcf13a89518715e4be842a6a3ac0
- Generate missing man pages
  related: #1211266

* Mon Jun 29 2015 jchaloup <jchaloup@redhat.com> - 0.20.0-0.2.git1c0b765
- Bump to upstream 1c0b765df6dabfe9bd0e20489ed3bd18e6b3bda8
  Comment out missing man pages
  related: #1211266

* Fri Jun 26 2015 jchaloup <jchaloup@redhat.com> - 0.20.0-0.1.git8ebd896
- Bump to upstream 8ebd896351513d446d56bc5785c070d2909226a3
  related: #1211266

* Fri Jun 26 2015 jchaloup <jchaloup@redhat.com> - 0.19.3-0.6.git712f303
- Bump to upstream 712f303350b35e70a573f3cb19193c8ec7ee7544
  related: #1211266

* Thu Jun 25 2015 jchaloup <jchaloup@redhat.com> - 0.19.3-0.5.git2803b86
- Bump to upstream 2803b86a42bf187afa816a7ce14fec754cc2af51
  related: #1211266

* Wed Jun 24 2015 Eric Paris <eparis@redhat.com> - 0.19.3-0.4.git5b4dc4e
- Set CAP_NET_BIND_SERVICE on the kube-apiserver so it can use 443

* Wed Jun 24 2015 jchaloup <jchaloup@redhat.com> - 0.19.3-0.3.git5b4dc4e
- Bump to upstream 5b4dc4edaa14e1ab4e3baa19df0388fa54dab344
  pkg/cloudprovider/* packages does not conform to golang language specification
  related: #1211266

* Tue Jun 23 2015 jchaloup <jchaloup@redhat.com> - 0.19.3-0.2.gita2ce3ea
- Bump to upstream a2ce3ea5293553b1fe0db3cbc6d53bdafe061d79
  related: #1211266

* Mon Jun 22 2015 jchaloup <jchaloup@redhat.com> - 0.19.1-0.1.gitff0546d
- Bump to upstream ff0546da4fc23598de59db9f747c535545036463
  related: #1211266

* Fri Jun 19 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.7.gitb2e9fed
- Bump to upstream b2e9fed3490274509506285bdba309c50afb5c39
  related: #1211266

* Thu Jun 18 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.6.gitf660940
- Bump to upstream f660940dceb3fe6ffb1b14ba495a47d91b5cd910
  related: #1211266

* Wed Jun 17 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.5.git43889c6
- Bump to upstream 43889c612c4d396dcd8fbf3fbd217e106eaf5bce
  related: #1211266

* Tue Jun 16 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.4.gita8269e3
- Bump to upstream a8269e38c9e2bf81ba18cd6420e2309745d5b0b9
  related: #1211266

* Sun Jun 14 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.3.git5e5c1d1
- Bump to upstream 5e5c1d10976f2f26d356ca60ef7d0d715c9f00a2
  related: #1211266

* Fri Jun 12 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.2.git0ca96c3
- Bump to upstream 0ca96c3ac8b47114169f3b716ae4521ed8c7657c
  related: #1211266

* Thu Jun 11 2015 jchaloup <jchaloup@redhat.com> - 0.19.0-0.1.git5a02fc0
- Bump to upstream 5a02fc07d8a943132b9e68fe7169778253318487
  related: #1211266

* Wed Jun 10 2015 jchaloup <jchaloup@redhat.com> - 0.18.2-0.3.git0dfb681
- Bump to upstream 0dfb681ba5d5dba535895ace9d650667904b5df7
  related: #1211266

* Tue Jun 09 2015 jchaloup <jchaloup@redhat.com> - 0.18.2-0.2.gitb68e08f
- golang-cover is not needed

* Tue Jun 09 2015 jchaloup <jchaloup@redhat.com> - 0.18.2-0.1.gitb68e08f
- Bump to upstream b68e08f55f5ae566c4ea3905d0993a8735d6d34f
  related: #1211266

* Sat Jun 06 2015 jchaloup <jchaloup@redhat.com> - 0.18.1-0.3.git0f1c4c2
- Bump to upstream 0f1c4c25c344f70c3592040b2ef092ccdce0244f
  related: #1211266

* Fri Jun 05 2015 jchaloup <jchaloup@redhat.com> - 0.18.1-0.2.git7309e1f
- Bump to upstream 7309e1f707ea5dd08c51f803037d7d22c20e2b92
  related: #1211266

* Thu Jun 04 2015 jchaloup <jchaloup@redhat.com> - 0.18.1-0.1.gita161edb
- Bump to upstream a161edb3960c01ff6e14813858c2eeb85910009b
  related: #1211266

* Wed Jun 03 2015 jchaloup <jchaloup@redhat.com> - 0.18.0-0.3.gitb5a91bd
- Bump to upstream b5a91bda103ed2459f933959241a2b57331747ba
- Don't run %check section (kept only for local run). Tests are now handled via CI.
  related: #1211266

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0.18.0-0.2.git5520386
- Bump to upstream 5520386b180d3ddc4fa7b7dfe6f52642cc0c25f3
  related: #1211266

* Mon Jun 01 2015 jchaloup <jchaloup@redhat.com> - 0.18.0-0.1.git0bb78fe
- Bump to upstream 0bb78fe6c53ce38198cc3805c78308cdd4805ac8
  related: #1211266

* Fri May 29 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-6
- Bump to upstream ed4898d98c46869e9cbdb44186dfdeda9ff80cc2
  related: #1211266

* Thu May 28 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-5
- Bump to upstream 6fa2777e26559fc008eacac83eb165d25bd9a7de
  related: #1211266

* Tue May 26 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-4
- Bump to upstream 01fcb58673001e56c69e128ab57e0c3f701aeea5
  related: #1211266

* Mon May 25 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-3
- Decompose package into master and node subpackage.
  Thanks to Avesh for testing and patience.
  related: #1211266

* Mon May 25 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-2
- Bump to upstream cf7b0bdc2a41d38613ac7f8eeea91cae23553fa2
  related: #1211266

* Fri May 22 2015 jchaloup <jchaloup@redhat.com> - 0.17.1-1
- Bump to upstream d9d12fd3f7036c92606fc3ba9046b365212fcd70
  related: #1211266

* Wed May 20 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-12
- Bump to upstream a76bdd97100c66a46e2b49288540dcec58a954c4
  related: #1211266

* Tue May 19 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-11
- Bump to upstream 10339d72b66a31592f73797a9983e7c207481b22
  related: #1211266

* Mon May 18 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-10
- Bump to upstream efb42b302d871f7217394205d84e5ae82335d786
  related: #1211266

* Sat May 16 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-9
- Bump to upstream d51e131726b925e7088b90915e99042459b628e0
  related: #1211266

* Fri May 15 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-8
- Bump to upstream 1ee33ac481a14db7b90e3bbac8cec4ceea822bfb
  related: #1211266

* Fri May 15 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-7
- Bump to upstream d3c6fb0d6a13c0177dcd67556d72963c959234ea
  related: #1211266

* Fri May 15 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-6
- Bump to upstream f57f31783089f41c0bdca8cb87a1001ca94e1a45
  related: #1211266

* Thu May 14 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-5
- Bump to upstream c90d381d0d5cf8ab7b8412106f5a6991d7e13c7d
  related: #1211266

* Thu May 14 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-4
- Bump to upstream 5010b2dde0f9b9eb820fe047e3b34bc9fa6324de
- Add debug info
  related: #1211266

* Wed May 13 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-3
- Bump to upstream ec19d41b63f5fe7b2c939e7738a41c0fbe65d796
  related: #1211266

* Tue May 12 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-2
- Provide /usr/bin/kube-version-change binary
  related: #1211266

* Tue May 12 2015 jchaloup <jchaloup@redhat.com> - 0.17.0-1
- Bump to upstream 962f10ee580eea30e5f4ea725c4e9e3743408a58
  related: #1211266

* Mon May 11 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-7
- Bump to upstream 63182318c5876b94ac9b264d1224813b2b2ab541
  related: #1211266

* Fri May 08 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-6
- Bump to upstream d136728df7e2694df9e082902f6239c11b0f2b00
- Add NetworkManager as dependency for /etc/resolv.conf
  related: #1211266

* Thu May 07 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-5
- Bump to upstream ca0f678b9a0a6dc795ac7a595350d0dbe9d0ac3b
  related: #1211266

* Wed May 06 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-4
- Add docs to kubernetes-unit-test
  related: #1211266

* Wed May 06 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-3
- Bump to upstream 3a24c0e898cb3060d7905af6df275a3be562451d
  related: #1211266

* Tue May 05 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-2
- Add api and README.md to kubernetes-unit-test
  related: #1211266

* Tue May 05 2015 jchaloup <jchaloup@redhat.com> - 0.16.2-1
- Bump to upstream 72048a824ca16c3921354197953fabecede5af47
  related: #1211266

* Mon May 04 2015 jchaloup <jchaloup@redhat.com> - 0.16.1-2
- Bump to upstream 1dcd80cdf3f00409d55cea1ef0e7faef0ae1d656
  related: #1211266

* Sun May 03 2015 jchaloup <jchaloup@redhat.com> - 0.16.1-1
- Bump to upstream 86751e8c90a3c0e852afb78d26cb6ba8cdbc37ba
  related: #1211266

* Fri May 01 2015 jchaloup <jchaloup@redhat.com> - 0.16.0-2
- Bump to upstream 72708d74b9801989ddbdc8403fc5ba4aafb7c1ef
  related: #1211266

* Wed Apr 29 2015 jchaloup <jchaloup@redhat.com> - 0.16.0-1
- Bump to upstream 7dcce2eeb7f28643d599c8b6a244523670d17c93
  related: #1211266

* Tue Apr 28 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-10
- Add unit-test subpackage
  related: #1211266

* Tue Apr 28 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-9
- Bump to upstream 99fc906f78cd2bcb08536c262867fa6803f816d5
  related: #1211266

* Mon Apr 27 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-8
- Bump to upstream 051dd96c542799dfab39184d2a7c8bacf9e88d85
  related: #1211266

* Fri Apr 24 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-7
- Bump to upstream 9f753c2592481a226d72cea91648db8fb97f0da8
  related: #1211266

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-6
- Bump to upstream cf824ae5e07965ba0b4b15ee88e08e2679f36978
  related: #1211266

* Tue Apr 21 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-5
- Bump to upstream 21788d8e6606038a0a465c97f5240b4e66970fbb
  related: #1211266

* Mon Apr 20 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-4
- Bump to upstream eb1ea269954da2ce557f3305fa88d42e3ade7975
  related: #1211266

* Fri Apr 17 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-3
- Obsolete cadvisor as it is integrated in kubelet
  related: #1211266

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-0.2.git0ea87e4
- Bump to upstream 0ea87e486407298dc1e3126c47f4076b9022fb09
  related: #1211266

* Tue Apr 14 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-0.1.gitd02139d
- Bump to upstream d02139d2b454ecc5730cc535d415c1963a7fb2aa
  related: #1211266

* Sun Apr 12 2015 jchaloup <jchaloup@redhat.com> - 0.14.2-0.2.gitd577db9
- Bump to upstream d577db99873cbf04b8e17b78f17ec8f3a27eca30

* Wed Apr 08 2015 jchaloup <jchaloup@redhat.com> - 0.14.2-0.1.git2719194
- Bump to upstream 2719194154ffd38fd1613699a9dd10a00909957e
  Use etcd-2.0.8 and higher

* Tue Apr 07 2015 jchaloup <jchaloup@redhat.com> - 0.14.1-0.2.gitd2f4734
- Bump to upstream d2f473465738e6b6f7935aa704319577f5e890ba

* Thu Apr 02 2015 jchaloup <jchaloup@redhat.com> - 0.14.1-0.1.gita94ffc8
- Bump to upstream a94ffc8625beb5e2a39edb01edc839cb8e59c444

* Wed Apr 01 2015 jchaloup <jchaloup@redhat.com> - 0.14.0-0.2.git8168344
- Bump to upstream 81683441b96537d4b51d146e39929b7003401cd5

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 0.14.0-0.1.git9ed8761
- Bump to upstream 9ed87612d07f75143ac96ad90ff1ff68f13a2c67
- Remove [B]R from devel branch until the package has stable API

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.6.git8a7a127
- Bump to upstream 8a7a127352263439e22253a58628d37a93fdaeb2

* Fri Mar 27 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.5.git8d94c43
- Bump to upstream 8d94c43e705824f23791b66ad5de4ea095d5bb32
  resolves: #1205362

* Wed Mar 25 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.4.git455fe82
- Bump to upstream 455fe8235be8fd9ba0ce21bf4f50a69d42e18693

* Mon Mar 23 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.3.gitef75888
- Remove runtime dependency on etcd
  resolves: #1202923

* Sun Mar 22 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.2.gitef75888
- Bump to upstream ef758881d108bb53a128126c503689104d17f477

* Fri Mar 20 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.1.gita8f2cee
- Bump to upstream a8f2cee8c5418676ee33a311fad57d6821d3d29a

* Fri Mar 13 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.9.git53b25a7
- Bump to upstream 53b25a7890e31bdec6f2a95b32200d6cc27ae2ca
  fix kube-proxy.service and kubelet
  resolves: #1200919 #1200924

* Fri Mar 13 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.8.git39dceb1
- Bump to upstream 39dceb13a511a83963a766a439cb386d10764310

* Thu Mar 12 2015 Eric Paris <eparis@redhat.com> - 0.12.0-0.7.gita3fd0a9
- Move from /etc/tmpfiles.d to %{_tmpfilesdir}
  resolves: #1200969

* Thu Mar 12 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.6.gita3fd0a9
- Place contrib/init/systemd/tmpfiles.d/kubernetes.conf to /etc/tmpfiles.d/kubernetes.conf

* Thu Mar 12 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.5.gita3fd0a9
- Bump to upstream a3fd0a9fd516bb6033f32196ae97aaecf8c096b1

* Tue Mar 10 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.4.gita4d871a
- Bump to upstream a4d871a10086436557f804930812f2566c9d4d39

* Fri Mar 06 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.3.git2700871
- Bump to upstream 2700871b049d5498167671cea6de8317099ad406

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.2.git8b627f5
- Bump to upstream 8b627f516fd3e4f62da90d401ceb3d38de6f8077

* Tue Mar 03 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.1.gitecca426
- Bump to upstream ecca42643b91a7117de8cd385b64e6bafecefd65

* Mon Mar 02 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.5.git6c5b390
- Bump to upstream 6c5b390160856cd8334043344ef6e08568b0a5c9

* Sat Feb 28 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.4.git0fec31a
- Bump to upstream 0fec31a11edff14715a1efb27f77262a7c3770f4

* Fri Feb 27 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.3.git08402d7
- Bump to upstream 08402d798c8f207a2e093de5a670c5e8e673e2de

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.2.git86434b4
- Bump to upstream 86434b4038ab87ac40219562ad420c3cc58c7c6b

* Tue Feb 24 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.1.git754a2a8
- Bump to upstream 754a2a8305c812121c3845d8293efdd819b6a704
  turn off integration tests until "FAILED: unexpected endpoints:
  timed out waiting for the condition" problem is resolved
  Adding back devel subpackage ([B]R list outdated)

* Fri Feb 20 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.3.git4c87805
- Bump to upstream 4c87805870b1b22e463c4bd711238ef68c77f0af

* Tue Feb 17 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.2.git6f84bda
- Bump to upstream 6f84bdaba853872dbac69c84d3ab4b6964e85d8c

* Tue Feb 17 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.1.git7d6130e
- Bump to upstream 7d6130edcdfabd7dd2e6a06fdc8fe5e333f07f5c

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.7.gitc9c98ab
- Bump to upstream c9c98ab19eaa6f0b2ea17152c9a455338853f4d0
  Since some dependencies are broken, we can not build Kubernetes from Fedora deps.
  Switching to vendored source codes until Go draft is resolved

* Wed Feb 04 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.6.git7f5ed54
- Bump to upstream 7f5ed541f794348ae6279414cf70523a4d5133cc

* Tue Feb 03 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.5.git2ac6bbb
- Bump to upstream 2ac6bbb7eba7e69eac71bd9acd192cda97e67641

* Mon Feb 02 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.4.gite335e2d
- Bump to upstream e335e2d3e26a9a58d3b189ccf41ceb3770d1bfa9

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.3.git55793ac
- Bump to upstream 55793ac2066745f7243c666316499e1a8cf074f0

* Thu Jan 29 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.2.gitca6de16
- Bump to upstream ca6de16df7762d4fc9b4ad44baa78d22e3f30742

* Tue Jan 27 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.1.git3623a01
- Bump to upstream 3623a01bf0e90de6345147eef62894057fe04b29
- update tests for etcd-2.0

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0.8.2-571.gitb2f287c
+- Bump to upstream b2f287c259d856f4c08052a51cd7772c563aff77

* Thu Jan 22 2015 Eric Paris <eparis@redhat.com> - 0.8.2-570.gitb2f287c
- patch kubelet service file to use docker.service not docker.socket

* Wed Jan 21 2015 jchaloup <jchaloup@redhat.com> - 0.8.2-0.1.git5b04640
- Bump to upstream 5b046406a957a1e7eda7c0c86dd7a89e9c94fc5f

* Sun Jan 18 2015 jchaloup <jchaloup@redhat.com> - 0.8.0-126.0.git68298f0
- Add some missing dependencies
- Add devel subpackage

* Fri Jan 09 2015 Eric Paris <eparis@redhat.com> - 0.8.0-125.0.git68298f0
- Bump to upstream 68298f08a4980f95dfbf7b9f58bfec1808fb2670

* Tue Dec 16 2014 Eric Paris <eparis@redhat.com> - 0.7.0-18.0.git52e165a
- Bump to upstream 52e165a4fd720d1703ebc31bd6660e01334227b8

* Mon Dec 15 2014 Eric Paris <eparis@redhat.com> - 0.6-297.0.git5ef34bf
- Bump to upstream 5ef34bf52311901b997119cc49eff944c610081b

* Wed Dec 03 2014 Eric Paris <eparis@redhat.com>
- Replace patch to use old googlecode/go.net/ with BuildRequires on golang.org/x/net/

* Tue Dec 02 2014 Eric Paris <eparis@redhat.com> - 0.6-4.0.git993ef88
- Bump to upstream 993ef88eec9012b221f79abe8f2932ee97997d28

* Mon Dec 01 2014 Eric Paris <eparis@redhat.com> - 0.5-235.0.git6aabd98
- Bump to upstream 6aabd9804fb75764b70e9172774002d4febcae34

* Wed Nov 26 2014 Eric Paris <eparis@redhat.com> - 0.5-210.0.gitff1e9f4
- Bump to upstream ff1e9f4c191342c24974c030e82aceaff8ea9c24

* Tue Nov 25 2014 Eric Paris <eparis@redhat.com> - 0.5-174.0.git64e07f7
- Bump to upstream 64e07f7fe03d8692c685b09770c45f364967a119

* Mon Nov 24 2014 Eric Paris <eparis@redhat.com> - 0.5-125.0.git162e498
- Bump to upstream 162e4983b947d2f6f858ca7607869d70627f5dff

* Fri Nov 21 2014 Eric Paris <eparis@redhat.com> - 0.5-105.0.git3f74a1e
- Bump to upstream 3f74a1e9f56b3c3502762930c0c551ccab0557ea

* Thu Nov 20 2014 Eric Paris <eparis@redhat.com> - 0.5-65.0.gitc6158b8
- Bump to upstream c6158b8aa9c40fbf1732650a8611429536466b21
- include go-restful build requirement

* Tue Nov 18 2014 Eric Paris <eparis@redhat.com> - 0.5-14.0.gitdf0981b
- Bump to upstream df0981bc01c5782ad30fc45cb6f510f365737fc1

* Tue Nov 11 2014 Eric Paris <eparis@redhat.com> - 0.4-680.0.git30fcf24
- Bump to upstream 30fcf241312f6d0767c7d9305b4c462f1655f790

* Mon Nov 10 2014 Eric Paris <eparis@redhat.com> - 0.4-633.0.git6c70227
- Bump to upstream 6c70227a2eccc23966d32ea6d558ee05df46e400

* Fri Nov 07 2014 Eric Paris <eparis@redhat.com> - 0.4-595.0.gitb695650
- Bump to upstream b6956506fa2682afa93770a58ea8c7ba4b4caec1

* Thu Nov 06 2014 Eric Paris <eparis@redhat.com> - 0.4-567.0.git3b1ef73
- Bump to upstream 3b1ef739d1fb32a822a22216fb965e22cdd28e7f

* Thu Nov 06 2014 Eric Paris <eparis@redhat.com> - 0.4-561.0.git06633bf
- Bump to upstream 06633bf4cdc1ebd4fc848f85025e14a794b017b4
- Make spec file more RHEL/CentOS friendly

* Tue Nov 04 2014 Eric Paris <eparis@redhat.com - 0.4-510.0.git5a649f2
- Bump to upstream 5a649f2b9360a756fc8124897d3453a5fa9473a6

* Mon Nov 03 2014 Eric Paris <eparis@redhat.com - 0.4-477.0.gita4abafe
- Bump to upstream a4abafea02babc529c9b5b9c825ba0bb3eec74c6

* Mon Nov 03 2014 Eric Paris <eparis@redhat.com - 0.4-453.0.git808be2d
- Bump to upstream 808be2d13b7bf14a3cf6985bc7c9d02f48a3d1e0
- Includes upstream change to remove --machines from the APIServer
- Port to new build system
- Start running %check tests again

* Fri Oct 31 2014 Eric Paris <eparis@redhat.com - 0.4+-426.0.gita18cdac
- Bump to upstream a18cdac616962a2c486feb22afa3538fc3cf3a3a

* Thu Oct 30 2014 Eric Paris <eparis@redhat.com - 0.4+-397.0.git78df011
- Bump to upstream 78df01172af5cc132b7276afb668d31e91e61c11

* Wed Oct 29 2014 Eric Paris <eparis@redhat.com - 0.4+-0.9.git8e1d416
- Bump to upstream 8e1d41670783cb75cf0c5088f199961a7d8e05e5

* Tue Oct 28 2014 Eric Paris <eparis@redhat.com - 0.4-0.8.git1c61486
- Bump to upstream 1c61486ec343246a81f62b4297671217c9576df7

* Mon Oct 27 2014 Eric Paris <eparis@redhat.com - 0.4-0.7.gitdc7e3d6
- Bump to upstream dc7e3d6601a89e9017ca9db42c09fd0ecb36bb36

* Fri Oct 24 2014 Eric Paris <eparis@redhat.com - 0.4-0.6.gite46af6e
- Bump to upstream e46af6e37f6e6965a63edb8eb8f115ae8ef41482

* Thu Oct 23 2014 Eric Paris <eparis@redhat.com - 0.4-0.5.git77d2815
- Bump to upstream 77d2815b86e9581393d7de4379759c536df89edc

* Wed Oct 22 2014 Eric Paris <eparis@redhat.com - 0.4-0.4.git97dd730
- Bump to upstream 97dd7302ac2c2b9458a9348462a614ebf394b1ed
- Use upstream kubectl bash completion instead of in-repo
- Fix systemd_post and systemd_preun since we are using upstream service files

* Tue Oct 21 2014 Eric Paris <eparis@redhat.com - 0.4-0.3.gite868642
- Bump to upstream e8686429c4aa63fc73401259c8818da168a7b85e

* Mon Oct 20 2014 Eric Paris <eparis@redhat.com - 0.4-0.2.gitd5377e4
- Bump to upstream d5377e4a394b4fc6e3088634729b538eac124b1b
- Use in tree systemd unit and Environment files
- Include kubectl bash completion from outside tree

* Fri Oct 17 2014 Eric Paris <eparis@redhat.com - 0.4-0.1.gitb011263
- Bump to upstream b01126322b826a15db06f6eeefeeb56dc06db7af
- This is a major non backward compatible change.

* Thu Oct 16 2014 Eric Paris <eparis@redhat.com> - 0.4-0.0.git4452163
- rebase to v0.4
- include man pages

* Tue Oct 14 2014 jchaloup <jchaloup@redhat.com> - 0.3-0.3.git98ac8e1
- create /var/lib/kubelet
- Use bash completions from upstream
- Bump to upstream 98ac8e178fcf1627399d659889bcb5fe25abdca4
- all by Eric Paris

* Mon Sep 29 2014 Jan Chaloupka <jchaloup@redhat.com> - 0.3-0.2.git88fdb65
- replace * with coresponding files
- remove dependency on gcc

* Wed Sep 24 2014 Eric Paris <eparis@redhat.com - 0.3-0.1.git88fdb65
- Bump to upstream 88fdb659bc44cf2d1895c03f8838d36f4d890796

* Tue Sep 23 2014 Eric Paris <eparis@redhat.com - 0.3-0.0.gitbab5082
- Bump to upstream bab5082a852218bb65aaacb91bdf599f9dd1b3ac

* Fri Sep 19 2014 Eric Paris <eparis@redhat.com - 0.2-0.10.git06316f4
- Bump to upstream 06316f486127697d5c2f5f4c82963dec272926cf

* Thu Sep 18 2014 Eric Paris <eparis@redhat.com - 0.2-0.9.gitf7a5ec3
- Bump to upstream f7a5ec3c36bd40cc2216c1da331ab647733769dd

* Wed Sep 17 2014 Eric Paris <eparis@redhat.com - 0.2-0.8.gitac8ee45
- Try to intelligently determine the deps

* Wed Sep 17 2014 Eric Paris <eparis@redhat.com - 0.2-0.7.gitac8ee45
- Bump to upstream ac8ee45f4fc4579b3ed65faafa618de9c0f8fb26

* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.2-0.5.git24b5b7e
- Bump to upstream 24b5b7e8d3a8af1eecf4db40c204e3c15ae955ba

* Thu Sep 11 2014 Eric Paris <eparis@redhat.com - 0.2-0.3.gitcc7999c
- Bump to upstream cc7999c00a40df21bd3b5e85ecea3b817377b231

* Wed Sep 10 2014 Eric Paris <eparis@redhat.com - 0.2-0.2.git60d4770
- Add bash completions

* Wed Sep 10 2014 Eric Paris <eparis@redhat.com - 0.2-0.1.git60d4770
- Bump to upstream 60d4770127d22e51c53e74ca94c3639702924bd2

* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-0.4.git6ebe69a
- prefer autosetup instead of setup (revert setup change in 0-0.3.git)
https://fedoraproject.org/wiki/Autosetup_packaging_draft
- revert version number to 0.1

* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.3.git6ebe69a
- gopath defined in golang package already
- package owns /etc/kubernetes
- bash dependency implicit
- keep buildroot/$RPM_BUILD_ROOT macros consistent
- replace with macros wherever possible
- set version, release and source tarball prep as per
https://fedoraproject.org/wiki/Packaging:SourceURL#Github

* Mon Sep 08 2014 Eric Paris <eparis@redhat.com>
- make services restart automatically on error

* Sat Sep 06 2014 Eric Paris <eparis@redhat.com - 0.1-0.1.0.git6ebe69a8
- Bump to upstream 6ebe69a8751508c11d0db4dceb8ecab0c2c7314a

* Wed Aug 13 2014 Eric Paris <eparis@redhat.com>
- update to upstream
- redo build to use project scripts
- use project scripts in %check
- rework deletion of third_party packages to easily detect changes
- run apiserver and controller-manager as non-root

* Mon Aug 11 2014 Adam Miller <maxamillion@redhat.com>
- update to upstream
- decouple the rest of third_party

* Thu Aug 7 2014 Eric Paris <eparis@redhat.com>
- update to head
- update package to include config files

* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
