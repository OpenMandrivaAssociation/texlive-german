%global tl_name german
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5e
Release:	%{tl_revision}.1
Summary:	Support for German typography
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/german
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/german.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/german.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/german.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Supports the old German orthography (alte deutsche Rechtschreibung).

