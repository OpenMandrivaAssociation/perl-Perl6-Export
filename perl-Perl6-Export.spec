%define upstream_name    Perl6-Export
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Implements the Perl 6 is export trait
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/Perl6-Export/
Source0:    http://www.cpan.org/modules/by-module/Perl6/Perl6-Export-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module prototypes the Perl 6 'exported' and 'exportable' traits
in Perl 5.

Instead of messing around with @EXPORT arrays, you just declare which subs
are to be exported (or are exportable on request) as part of those subs.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes y | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Export.pm
