from docx import Document

def merge_consecutive_tables(doc):
    # Helper function to append the rows from one table to another
    def append_table_rows(source_table, target_table):
        for row in source_table.rows:
            target_row = target_table.add_row().cells
            for i, cell in enumerate(row.cells):
                target_row[i].text = cell.text
    
    # Get all the elements (paragraphs, tables, etc.) in the document
    elements = list(doc.element.body)

    i = 0
    while i < len(elements) - 1:
        current_element = elements[i]
        next_element = elements[i + 1]

        # Check if the current and next elements are tables
        if current_element.tag.endswith('tbl') and next_element.tag.endswith('tbl'):
            # Convert elements back to table objects
            current_table = doc.tables[i]
            next_table = doc.tables[i + 1]

            # Append rows of the next table to the current table
            append_table_rows(next_table, current_table)

            # Remove the next table from the document
            doc.element.body.remove(next_table._element)

            # After merging, the list of elements has one less element, so don't increment i
            elements = list(doc.element.body)
        else:
            i += 1

    # Save the modified document (optional)
    # doc.save('merged_tables_document.docx')

    return doc

# Example usage
doc = Document('your_document.docx')
merged_doc = merge_consecutive_tables(doc)
merged_doc.save('merged_tables_document.docx')
