%define realname Perl6-Export

Summary: Implements the Perl 6 is export trait
Name: perl-Perl6-Export
Version: 0.07
Release: %mkrel 1
License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/dist/Perl6-Export/
Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Export-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
This module prototypes the Perl 6 'exported' and 'exportable' traits
in Perl 5.

Instead of messing around with @EXPORT arrays, you just declare which subs
are to be exported (or are exportable on request) as part of those subs.

%prep
%setup -q -n %{realname}-%{version}

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
