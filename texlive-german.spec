Name:		texlive-german
Version:	42428
Release:	1
Summary:	Support for German typography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/german
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/german.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Supports the new German orthography (neue deutsche
Rechtschreibung).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/german/german.sty
%{_texmfdistdir}/tex/generic/german/ngerman.sty
%doc %{_texmfdistdir}/doc/generic/german/00readme.1st
%doc %{_texmfdistdir}/doc/generic/german/betatest/00readme.1st
%doc %{_texmfdistdir}/doc/generic/german/gerdoc.pdf
%doc %{_texmfdistdir}/doc/generic/german/gerdoc.tex
%doc %{_texmfdistdir}/doc/generic/german/german.MISSING
%doc %{_texmfdistdir}/doc/generic/german/hyphxmpl.cfg
#- source
%doc %{_texmfdistdir}/source/generic/german/german.dtx
%doc %{_texmfdistdir}/source/generic/german/german.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
