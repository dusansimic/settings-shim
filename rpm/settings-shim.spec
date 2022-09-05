%define _appid com.github.cassidyjames.settings-shim

Name:           settings-shim
Version:        0.1.0
Release:        1%{?dist}
Summary:        Simple shim to launch GNOME Control Center from the settings spec

License:        GPL3
URL:            https://github.com/dusansimic/settings-shim
Source0:        %{url}/archive/refs/heads/master.zip

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gtk3-devel

%description
%{summary}.

%prep
%autosetup -n %{name}-master

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/%{_appid}
%{_datadir}/applications/%{_appid}.desktop

%changelog

