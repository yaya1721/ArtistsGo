import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>New Work</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="post-create_date">Author</Label>
              <Input
                type="text"
                id="post-author"
                name="author"
                value={this.state.activeItem.author}
                onChange={this.handleChange}
              />
            </FormGroup>
             <FormGroup>
              <Label for="post-create_date">Date</Label>
              <Input
                type="date"
                id="post-create_date"
                name="date"
                value={this.state.activeItem.create_date}
                onChange={this.handleChange}
              />
            </FormGroup>
            <FormGroup> 
              <Label for="post-create_date">Category</Label>
              <Input
                type="text"
                id="post-category"
                name="category"
                value={this.state.activeItem.category}
                onChange={this.handleChange}
              />
            </FormGroup>
             <FormGroup>
              <Label for="post-title">Title</Label>
              <Input
                type="text"
                id="post-title"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter work title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="post-description">Description</Label>
              <Input
                type="text"
                id="post-description"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter work description"
              />
            </FormGroup>
             <FormGroup>
              <Label for="post-description">Content</Label>
              <Input
                type="file"
                id="post-content"
                name="content"
                value={this.state.activeItem.content}
                onChange={this.handleChange}
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}