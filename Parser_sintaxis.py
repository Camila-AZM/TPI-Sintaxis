import ply.yacc as yacc
import xml.etree.ElementTree as ET
from Lexer_sintaxis import tokens

def p_docbook(p):
    '''docbook: TipoDocumento article''' 

def p_article(p):
    '''article: A_Article metadata items sections C_Article
        | A_Article items sections C_Article
        | A_Article items C_Article'''

def p_metadata(p):
    '''metadata: A_Info info C_Info A_Title title C_Title
        | A_Title title C_Title
        | A_Info info C_Info'''

def p_items(p):
    '''items: A_ItemizedList items C_ItemizedList
        | A_ItemizedList items C_ItemizedList items 
        | A_Important important C_Important
        | A_Important important C_Important items
        | paragraph
        | paragraph items
        | A_Address address C_Address
        | A_Address address C_Address items
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject items
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable items
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment items
        | A_Abstract title paragraph C_Abstract
        | A_Abstract title paragraph C_Abstract items
        | A_Abstract paragraph C_Abstract
        | A_Abstract paragraph C_Abstract items'''



def p_sections(p):
    '''section: A_Section contenidosection C_Section
        | A_Section contenidosection C_Section section
        | A_SimpleSection contenidosimpsection C_SimpleSection
        | A_SimpleSection contenidosimpsection C_SimpleSection section'''

def p_contenidosection(p):
    '''contenidosection: metadata items section
        | metadata items
        | metadata section
        | metadata'''

def p_contenidosimpsection(p):
    '''contenidosimpsection: metadata items
        | metadata'''

def p_info(p):
    '''info: A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject info
        | A_Abstract abstract C_Abstract
        | A_Abstract abstract C_Abstract info
        | A_Address address C_Address
        | A_Address address C_Address info
        | A_Author author C_Author
        | A_Author author C_Author info
        | A_Date personalinfo C_Date
        | A_Date personalinfo C_Date info
        | A_Copyright copyright C_Copyright
        | A_Copyright copyright C_Copyright info 
        | A_Title title C_Title
        | A_Title title C_Title info'''
    
def p_title(p):
    '''title: Contenido
        | Contenido title
        | A_Emphasis emphasis C_Emphasis
        | A_Emphasis emphasis C_Emphasis title
        | A_Link link C_Link
        | A_Link link C_Link title
        | A_Email email C_Email
        | A_Email email C_Email title'''

def p_important(p):
    '''important: A_Title title C_Title items
        | items'''

def p_paragraph(p):
    '''paragraph: A_Para para C_Para
        | A_Simpara inlinetags C_Simpara
        | A_Para para C_Para paragraph
        | A_Simpara inlinetags C_Simpara paragraph'''
    
def p_mediaobject(p):
    '''mediaobject: info multimedia
        | multimedia'''

def p_personalinfo(p):
    '''personalinfo: Contenido
        | Contenido personalinfo
        | '''

def p_para(p):
    '''para: Contenido 
        | Contenido para
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis para
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link para
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link para
        | A_Author author C_Author
        | A_Author author C_Author para
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment para
        | A_ItemizedList items C_ItemizedList
        | A_ItemizedList items C_ItemizedList para
        | A_Important  items C_Important
        | A_Important items C_Important para
        | A_Address address C_Address
        | A_Address address C_Address para
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject para
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable para'''

def p_inlinetags(p):
    '''inlinetags: Contenido
        | Contenido inlinetags
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis inlinetags
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link inlinetags
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment inlinetags
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email inlinetags
        | A_Author author C_Author
        | A_Author author C_Author inlinetags'''

def p_abstract(p):
    '''abstract: A_Title title C_title paragraph
        | paragraph'''
    
def p_address(p):
    '''address: Contenido 
        | Contenido address 
        | A_Street personalinfo C_Street 
        | A_Street personalinfo C_Street address
        | A_City personalinfo C_City
        | A_City personalinfo C_City address
        | A_State personalinfo C_State
        | A_State personalinfo C_State address
        | A_Phone personalinfo C_Phone 
        | A_Phone personalinfo C_Phone address 
        | A_Email personalinfo C_Email
        | A_Email personalinfo C_Email address'''

def author(p):
    '''author: A_FirstName personalinfo C_FirstName
        | A_FirstName personalinfo C_FirstName author
        | A_SurName personalinfo C_SurName
        | A_SurName personalinfo C_SurName author'''

def p_copyright(p):
    '''copyright: A_Year personalinfo C_Year
        | A_Year personalinfo C_Year A_Holder personalinfo C_Holder
        | A_Year personalinfo C_Year copyright
        | A_Year personalinfo C_Year copyright A_Holder personalinfo C_Holder'''
    
def p_personalinfo(p):
    '''personalinfo: Contenido
        | Contenido personalinfo
        | A_Link inlinetags C_Link
        | A_Link inlinetags C_Link personalinfo
        | A_Emphasis inlinetags C_Emphasis
        | A_Emphasis inlinetags C_Emphasis personalinfo
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment personalinfo'''

def p_multimedia(p):
    '''multimedia: A_ImageObject imageobject C_ImageObject
        | A_ImageObject imageobject C_ImageObject multimedia
        | A_VideoObject videoobject C_VideoObject
        | A_VideoObject videoobject C_VideoObject multimedia'''

def p_videoobject(p):
    '''videoobject: VideoData
        | Info VideoData'''

def p_imageobject(p):
    '''imageobject: ImageData
        | Info ImageData'''

def p_itemizedlist(p):
    '''itemizedlist: A_listitem listitem C_listitem'''

def p_listitem(p):
    '''listitem: items'''

def p_table(p):
    '''table: A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject table
        | A_Tgroup tgroup C_Tgroup
        | A_Tgroup tgroup C_Tgroup table'''

def p_tgroup(p):
    '''tgroup: A_Thead row C_Thead A_Tfoot row C_Tfoot A_Tbody row C_Tbody
        | A_Thead row C_Thead A_Tbody row C_Tbody
        | A_Tfoot row C_Tfoot A_Tbody row C_Tbody
        | A_Tbody row C_Tbody'''

def p_row(p):
    '''row: A_Row entries C_Row
    | A_Row entries C_Row row'''

def p_entries(p):
    '''entries: A_Entry entry C_Entry
        | A_Entry entry C_Entry entries
        | A_EntryTbl entrytbl C_EntryTbl
        | A_EntryTbl entrytbl C_EntryTbl entries'''

def p_entry(p):
    '''entry: Contenido entry
        | A_ItemizedList items C_ItemizedList
        | A_ItemizedList items C_ItemizedList entry 
        | A_Important important C_Important
        | A_Important important C_Important entry
        | paragraph
        | paragraph entry
        | A_MediaObject mediaobject C_MediaObject
        | A_MediaObject mediaobject C_MediaObject entry
        | A_InformalTable table C_InformalTable
        | A_InformalTable table C_InformalTable entry
        | A_Comment inlinetags C_Comment
        | A_Comment inlinetags C_Comment entry
        | A_Abstract title paragraph C_Abstract
        | A_Abstract title paragraph C_Abstract entry
        | A_Abstract paragraph C_Abstract
        | A_Abstract paragraph C_Abstract entry'''

def p_entrytbl(p):
    '''entrytbl: A_Thead row C_Thead A_Tbody row C_Tbody
        | A_Tbody row C_Tbody'''
    
def p_error_lexico(p):
    print("Error sintactico en la linea", p.lineno, "Valor:", p.value)

parser = yacc.yacc()
