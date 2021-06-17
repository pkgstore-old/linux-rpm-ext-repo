%global d_repos                 %{_sysconfdir}/yum.repos.d
%global release_prefix          100

Name:                           ext-repo
Version:                        1.0.6
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure repositories
License:                        MIT

Source10:                       elasticsearch.repo
Source11:                       mariadb.el.repo
Source12:                       mariadb.fc.repo
Source13:                       mysql.el.repo
Source14:                       mysql.fc.repo
Source15:                       remi.el.repo
Source16:                       remi.fc.repo
Source30:                       elrepo.repo
Source31:                       percona.repo

%description
META-package for install and configure repositories.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_repos}/elasticsearch.repo

%if 0%{?fedora}
%{__install} -Dp -m 0644 %{SOURCE12} \
  %{buildroot}%{d_repos}/mariadb.repo
%{__install} -Dp -m 0644 %{SOURCE14} \
  %{buildroot}%{d_repos}/mysql.repo
%{__install} -Dp -m 0644 %{SOURCE16} \
  %{buildroot}%{d_repos}/remi.repo
%endif

%if 0%{?rhel}
%{__install} -Dp -m 0644 %{SOURCE11} \
  %{buildroot}%{d_repos}/mariadb.repo
%{__install} -Dp -m 0644 %{SOURCE13} \
  %{buildroot}%{d_repos}/mysql.repo
%{__install} -Dp -m 0644 %{SOURCE15} \
  %{buildroot}%{d_repos}/remi.repo
%{__install} -Dp -m 0644 %{SOURCE30} \
  %{buildroot}%{d_repos}/elrepo.repo
%{__install} -Dp -m 0644 %{SOURCE31} \
  %{buildroot}%{d_repos}/percona.repo
%endif


%files
%config %{d_repos}/elasticsearch.repo
%config %{d_repos}/mariadb.repo
%config %{d_repos}/mysql.repo
%config %{d_repos}/remi.repo

%if 0%{?rhel}
%config %{d_repos}/elrepo.repo
%config %{d_repos}/percona.repo
%endif


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.6-100
- UPD: Move to GitHub.
- UPD: License.

* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.5-100
- UPD: Remi repository.

* Thu Jul 18 2019 Package Store <kitsune.solar@gmail.com> - 1.0.4-100
- NEW: Percona repository.

* Thu Jul 18 2019 Package Store <kitsune.solar@gmail.com> - 1.0.3-100
- NEW: PHP repository.

* Tue Jul 16 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- NEW: ELRepo repository.

* Thu Jul 04 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-103
- Update REPO-files.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-102
- Update SPEC-file.

* Mon Jul 01 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-101
- Update from MARKETPLACE.

* Sat Jun 22 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- Add MySQL repos.

* Thu Mar 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
